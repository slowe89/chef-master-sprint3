# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428097065.08886
_enable_loop = True
_template_filename = '/Users/spencerlowe/PycharmProjects/chef-master/rentals/templates/ItemDetails.html'
_template_uri = 'ItemDetails.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['page_title', 'tab_title', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        item = context.get('item', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def page_title():
            return render_page_title(context)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        date = context.get('date', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context)
        def content():
            return render_content(context)
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
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Standard Rental Price Per Day: $')
        __M_writer(str( item.standard_rental_price ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n            <div class="spacer"></div>\n            <div class="spacer"></div>\n\n\t\t</div>\n')
        __M_writer('\n')
        if item.quantity_on_hand > 0:
            __M_writer('                <div class="col-md-3">\n\n')
            if item.quantity_on_hand > 0:
                __M_writer('                    <div class="quantity_field">\n                        <paper-input-decorator class="short" floatingLabel label="Rental Duration">\n                            <input is="core-input" id="quantity" value="1"/>\n                        </paper-input-decorator>\n                    </div>\n')
                __M_writer('\n\n')
                __M_writer('                    <paper-button raised data-pid="')
                __M_writer(str( item.id ))
                __M_writer('" class="create_button add_button">Add to Cart</paper-button>\n')
            __M_writer('\n                </div>\n')
        else:
            __M_writer('            <p>\n                <b>This item is currently rented out.  It will be available ')
            __M_writer(str( date[0].due_date.strftime('%m/%d/%Y') ))
            __M_writer('</b>\n            </p>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/spencerlowe/PycharmProjects/chef-master/rentals/templates/ItemDetails.html", "uri": "ItemDetails.html", "line_map": {"128": 71, "129": 73, "130": 79, "131": 82, "132": 82, "133": 82, "134": 85, "135": 88, "136": 89, "137": 90, "138": 90, "139": 93, "140": 96, "141": 99, "142": 103, "148": 142, "27": 0, "41": 7, "42": 9, "47": 13, "57": 18, "64": 18, "65": 22, "66": 23, "67": 23, "68": 26, "74": 11, "81": 11, "82": 12, "83": 12, "89": 15, "100": 15, "101": 18, "106": 28, "107": 30, "108": 32, "109": 35, "110": 38, "111": 38, "112": 38, "113": 38, "114": 40, "115": 43, "116": 45, "117": 48, "118": 49, "119": 49, "120": 52, "121": 56, "122": 57, "123": 57, "124": 60, "125": 66, "126": 67, "127": 69}}
__M_END_METADATA
"""
