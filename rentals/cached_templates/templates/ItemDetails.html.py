# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427931606.436429
_enable_loop = True
_template_filename = '/Users/spencerlowe/PycharmProjects/chef-master/rentals/templates/ItemDetails.html'
_template_uri = 'ItemDetails.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'page_title', 'tab_title']


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
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        item = context.get('item', UNDEFINED)
        date = context.get('date', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context)
        item = context.get('item', UNDEFINED)
        date = context.get('date', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\t<div class="row main_row">\n\t\t\n')
        __M_writer('\t\t<div class="col-md-4">\n\t\t\t\n')
        __M_writer('\t\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer(str( item.specs.photograph.image ))
        __M_writer('" class="rental_image"/>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-5">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>')
        __M_writer(str( item.specs.description ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t\t<div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Standard Rental Price: $')
        __M_writer(str( item.standard_rental_price ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t\t<div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Price Per Day: $')
        __M_writer(str( item.price_per_day ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n            <div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Rental length: 30 Days</p>\n\t\t\t</div>\n')
        __M_writer('\n            <div class="spacer"></div>\n            <div class="spacer"></div>\n\n')
        if item.quantity_on_hand > 0:
            __M_writer('            <paper-button raised data-pid="')
            __M_writer(str( item.id ))
            __M_writer('" class="create_button add_button">Add to Cart</paper-button>\n')
        else:
            __M_writer('            <p>\n                This item is currently rented out.  It will be available ')
            __M_writer(str( date[0].due_date.strftime('%m/%d/%Y') ))
            __M_writer('\n            </p>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div class="row">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="col-md-8">\n\t\t\t\t<h1>')
        __M_writer(str( item.specs.name ))
        __M_writer('</h1>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tab_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def tab_title():
            return render_tab_title(context)
        __M_writer = context.writer()
        __M_writer('\n  \t')
        __M_writer(str( item.specs.name ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "ItemDetails.html", "filename": "/Users/spencerlowe/PycharmProjects/chef-master/rentals/templates/ItemDetails.html", "line_map": {"128": 26, "134": 11, "141": 11, "142": 12, "143": 12, "149": 143, "27": 0, "41": 7, "42": 9, "47": 13, "57": 15, "68": 15, "69": 18, "74": 28, "75": 30, "76": 32, "77": 35, "78": 38, "79": 38, "80": 38, "81": 38, "82": 40, "83": 43, "84": 45, "85": 48, "86": 49, "87": 49, "88": 52, "89": 56, "90": 57, "91": 57, "92": 60, "93": 64, "94": 65, "95": 65, "96": 68, "97": 72, "98": 76, "99": 80, "100": 82, "101": 82, "102": 82, "103": 84, "104": 85, "105": 86, "106": 86, "107": 89, "108": 92, "109": 95, "110": 98, "111": 102, "117": 18, "124": 18, "125": 22, "126": 23, "127": 23}}
__M_END_METADATA
"""
