# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428097504.61165
_enable_loop = True
_template_filename = '/Users/spencerlowe/PycharmProjects/chef-master/products/templates/ItemDetails.html'
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
        item = context.get('item', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def tab_title():
            return render_tab_title(context._locals(__M_locals))
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
        __M_writer('\n')
        __M_writer('\t\t\t<div class="col-md-4">\n\t\t\t\t\n\t\t\t</div>\n')
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
        __M_writer('\n  ')
        __M_writer(str( item.specs.name ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        item = context.get('item', UNDEFINED)
        def page_title():
            return render_page_title(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('" class="product_image"/>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-5">\n\t\t\t\n')
        __M_writer('\t\t\t<div class="product_info">\n\t\t\t\t<p>')
        __M_writer(str( item.specs.description ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t\t<div class="spacer"></div>\n\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Price: $')
        __M_writer(str( item.specs.price ))
        __M_writer('</p>\n\t\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t\t<div class="item_info">\n\t\t\t\t<p>Quantity Available:\n')
        if item.quantity_on_hand > 0:
            __M_writer('                        ')
            __M_writer(str( item.quantity_on_hand ))
            __M_writer('\n')
        else:
            __M_writer('                        NOT CURRENTLY AVAILABLE\n')
        __M_writer('                </p>\n\t\t\t</div>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n')
        __M_writer('\t\t<div class="col-md-3">\n\n')
        if item.quantity_on_hand > 0:
            __M_writer('\t\t\t<div class="quantity_field">\n\t\t\t\t<paper-input-decorator class="short" floatingLabel label="Quantity">\n\t\t\t\t\t<input is="core-input" id="quantity" value="1"/>\n\t\t\t\t</paper-input-decorator>\n\t\t\t</div>\n')
            __M_writer('\n')
            __M_writer('\t\t\t<paper-button raised data-pid="')
            __M_writer(str( item.id ))
            __M_writer('" class="create_button add_button">Add to Cart</paper-button>\n')
        __M_writer('\n\t\t</div>\n')
        __M_writer('\n\t</div>\n')
        __M_writer('\n\n')
        __M_writer('\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n\t<div class="spacer"></div>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/spencerlowe/PycharmProjects/chef-master/products/templates/ItemDetails.html", "uri": "ItemDetails.html", "line_map": {"128": 71, "129": 71, "130": 72, "131": 73, "132": 75, "133": 78, "134": 81, "135": 83, "136": 85, "137": 87, "138": 93, "139": 95, "140": 95, "141": 95, "142": 98, "143": 101, "144": 104, "145": 107, "146": 111, "152": 146, "27": 0, "40": 7, "41": 9, "46": 13, "56": 18, "63": 18, "64": 22, "65": 23, "66": 23, "67": 26, "68": 28, "69": 32, "75": 11, "82": 11, "83": 12, "84": 12, "90": 15, "100": 15, "101": 18, "106": 34, "107": 36, "108": 38, "109": 41, "110": 44, "111": 44, "112": 44, "113": 44, "114": 46, "115": 49, "116": 51, "117": 54, "118": 55, "119": 55, "120": 58, "121": 62, "122": 63, "123": 63, "124": 66, "125": 68, "126": 70, "127": 71}}
__M_END_METADATA
"""
