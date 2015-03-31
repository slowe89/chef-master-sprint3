# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427752620.632382
_enable_loop = True
_template_filename = '/Users/spencerlowe/PycharmProjects/chef-master/products/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['tab_title', 'page_title', 'content']


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
    return runtime._inherit_from(context, '/base_admin/templates/View.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        s_items = context.get('s_items', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        bulk_items = context.get('bulk_items', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'tab_title'):
            context['self'].tab_title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  Products\n')
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
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>View Items</h1>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t<paper-button class="create_button search_button" raised>Search</paper-button>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        s_items = context.get('s_items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
        bulk_items = context.get('bulk_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title">Bulk Items</h3>\n')
        __M_writer('\n')
        for item in bulk_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="product_image"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<hr>\n')
        __M_writer('\n')
        __M_writer('\t<h3 class="table_title clearfix">Individualized Items</h3>\n')
        __M_writer('\n')
        for item in s_items:
            __M_writer('\n\t\t<div class="item_box">\n\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><h4>')
            __M_writer(str( item.specs.name ))
            __M_writer('</h4></a>\n')
            __M_writer('\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t<div class="spacer"></div>\n\t\t\t\n')
            __M_writer('\t\t\t<a href="/products/products.details/')
            __M_writer(str( item.id ))
            __M_writer('"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer(str( item.specs.photograph.image ))
            __M_writer('" class="item_box"/></a>\n')
            __M_writer('\n\t\t</div>\n\n')
        __M_writer('\n')
        __M_writer('\t<div class="clearfix"></div>\n')
        __M_writer('\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 76, "129": 77, "130": 81, "131": 81, "132": 81, "133": 81, "134": 81, "135": 83, "136": 89, "137": 89, "138": 89, "139": 89, "140": 89, "141": 89, "142": 91, "143": 96, "144": 98, "145": 100, "146": 102, "147": 106, "153": 147, "27": 0, "41": 7, "42": 9, "47": 13, "57": 11, "63": 11, "69": 18, "75": 18, "76": 22, "77": 26, "78": 28, "79": 32, "85": 15, "96": 15, "97": 18, "102": 34, "103": 36, "104": 38, "105": 40, "106": 42, "107": 43, "108": 47, "109": 47, "110": 47, "111": 47, "112": 47, "113": 49, "114": 55, "115": 55, "116": 55, "117": 55, "118": 55, "119": 55, "120": 57, "121": 62, "122": 64, "123": 66, "124": 68, "125": 70, "126": 72, "127": 74}, "source_encoding": "ascii", "filename": "/Users/spencerlowe/PycharmProjects/chef-master/products/templates/products.html", "uri": "products.html"}
__M_END_METADATA
"""
