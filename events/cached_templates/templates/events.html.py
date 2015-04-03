# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428090759.777595
_enable_loop = True
_template_filename = '/Users/spencerlowe/PycharmProjects/chef-master/events/templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'extra_links', 'page_title', 'tab_title', 'paper_elements_import']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base_app/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        def paper_elements_import():
            return render_paper_elements_import(context._locals(__M_locals))
        def extra_links():
            return render_extra_links(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'paper_elements_import'):
            context['self'].paper_elements_import(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_links'):
            context['self'].extra_links(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        def page_title():
            return render_page_title(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-6">\n\n')
        __M_writer('\t\t\t<h3>Batch Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tBatch Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-button class="success_button run_batch" raised>Submit</paper-button>\n\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-6">\n\t\t\t\n')
        __M_writer('\t\t\t<h3>Filter Options</h3>\n\t\t\t\n\t\t\t<div class="dropdown">\n\t\t\t\t<button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropwdown" aria-expanded="true">\n\t\t\t\t\tFilter Options\n\t\t\t\t\t<span class="caret"></span>\n\t\t\t\t</button>\n\t\t\t\t<ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">\n\t\t\t\t\t<li role="presentation">Delete</li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t\t<paper-input-decorator class="short" floatingLabel label="Criteria">\n\t\t\t\t<input is="core-input"></input>\n\t\t\t</paper-input-decorator>\n\n\t\t\t<paper-button class="success_button apply_filter" raised>Submit</paper-button>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<table class="table table-hover table-bordered">\n\t\t<thead>\n\t\t\t<tr>\n\t\t\t\t<th>\n\t\t\t\t\t<paper-button raised class="">Select All</paper-button>\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tName\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tStart Date\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tVenue\n\t\t\t\t</th>\n\t\t\t\t<th>\n\t\t\t\t\tActions\n\t\t\t\t</th>\n\t\t\t</tr>\n\t\t</thead>\n\t\t<tbody>\n')
        for event in events:
            __M_writer('\t\t\t\t<tr>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<paper-checkbox></paper-checkbox>\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( event.event_template.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( event.start_date.strftime("%B %d, %Y") ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t')
            __M_writer(str( event.venue.name ))
            __M_writer('\n\t\t\t\t\t</td>\n\t\t\t\t\t<td>\n\t\t\t\t\t\t<a class="button" href="/events/areas.view/')
            __M_writer(str( event.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="success_button">Areas</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/events/venues.edit/')
            __M_writer(str( event.venue.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="success_button">Venue Info</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/events/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="edit_button">Edit</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t\t<a class="button" href="/events/events.delete/')
            __M_writer(str( event.id ))
            __M_writer('">\n\t\t\t\t\t\t\t<paper-button raised class="delete_button">Delete</paper-button>\n\t\t\t\t\t\t</a>\n\t\t\t\t\t</td>\n\t\t\t\t</tr>\n')
        __M_writer('\t\t</tbody>\n\t</table>\t\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_links():
            return render_extra_links(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_admin/styles/View.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>Scheduled Events</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<div class="create_button">\n\t\t\t\t\t<a class="button" href="/events/events.create/">\n\t\t\t\t\t\t<paper-button class="create_button" raised>Schedule an Event</paper-button>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Scheduled Events\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_paper_elements_import(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def paper_elements_import():
            return render_paper_elements_import(context)
        __M_writer = context.writer()
        __M_writer('\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-input/paper-input.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-button/paper-button.html">\n\t<link rel="import" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('base_app/styles/bower_components/paper-checkbox/paper-checkbox.html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/spencerlowe/PycharmProjects/chef-master/events/templates/events.html", "line_map": {"132": 21, "133": 22, "134": 22, "140": 28, "146": 28, "147": 32, "148": 36, "149": 38, "150": 47, "27": 0, "156": 11, "162": 11, "168": 15, "44": 7, "45": 9, "175": 15, "176": 16, "177": 16, "50": 13, "179": 17, "180": 18, "181": 18, "55": 19, "187": 181, "60": 23, "70": 25, "79": 25, "80": 28, "85": 49, "86": 51, "87": 53, "88": 56, "89": 59, "90": 74, "91": 77, "92": 79, "93": 82, "94": 100, "95": 103, "96": 106, "97": 108, "98": 110, "99": 112, "100": 133, "101": 134, "102": 139, "103": 139, "104": 142, "105": 142, "106": 145, "107": 145, "108": 148, "109": 148, "110": 151, "111": 151, "112": 154, "113": 154, "114": 157, "115": 157, "116": 163, "117": 166, "118": 168, "119": 172, "125": 21, "178": 17}, "uri": "events.html"}
__M_END_METADATA
"""
