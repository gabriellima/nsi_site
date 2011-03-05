import os
import time
from django.core.management import call_command
from django.conf import settings
from selenium.firefox.firefox_profile import FirefoxProfile
from splinter.browser import Browser
from lettuce import after, before, world
from web_steps import *

@before.harvest
def initial_run_time(variables):
    world.time_before_harvest = time.time()

@before.all
def set_browser():
    enable_selenium_specs_to_run_offline()
    world.browser = Browser()

def enable_selenium_specs_to_run_offline():
    prefs = FirefoxProfile._get_webdriver_prefs()
    prefs['network.manage-offline-status'] = 'false'

    @staticmethod
    def prefs_func():
        return prefs
    FirefoxProfile._get_webdriver_prefs = prefs_func

@before.each_scenario
def clean_database(scenario):
    clean_data()
    clean_media()

def clean_data():
    call_command('flush', interactive=False)
    call_command('loaddata', 'all')

def clean_media():
    clean_media_by_kind('images')
    clean_media_by_kind('files')

def clean_media_by_kind(kind):
    images_dir = os.path.join(settings.MEDIA_ROOT, kind)
    for file_name in os.listdir(images_dir):
        clean_all(os.path.join(images_dir, file_name))

def clean_all(directory):
    for file_name in os.listdir(directory):
        absname = os.path.join(directory, file_name)
        if os.path.isdir(absname) and file_name not in ['.', '..']:
            clean_all(absname)
        elif not file_name.startswith('.'):
            os.unlink(absname)

@after.all
def finish_him(total_result):
    world.browser.quit()
    clean_media()
    
@after.harvest
def run_time(results):
    time_after_harvest = time.time()
    time_before_harvest = world.time_before_harvest
    total_time = int(time_after_harvest - time_before_harvest)
    minutes = total_time / 60
    seconds = total_time % 60
    total_features_ran = 0
    total_scenarios_ran = 0
    total_scenarios_passed = 0
    total_scenarios_failed = dict()
    for app in results:
        total_features_ran += app.features_ran
        total_scenarios_ran += app.scenarios_ran
        total_scenarios_passed += app.scenarios_passed
        for result in app.scenario_results:
            if result.passed == False:
                total_scenarios_failed.update({result.scenario.name: result.scenario.feature})

    print '-------------------------------------------------'
    print '%i features ran.' % total_features_ran
    print '%i scenarios ran.' % total_scenarios_ran
    print '%i scenarios passed.' % total_scenarios_passed
    if total_scenarios_failed:
        print 'Error in:'
        for scenario, feature in total_scenarios_failed.iteritems():
            print feature.name + ' ~> ' + scenario
    else:
        print 'No errors! Congratulations!'
    print 'Everything ran in %i minute(s) and %i second(s).' % (minutes, seconds)
    print '-------------------------------------------------'
