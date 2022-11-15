# -*- coding: utf-8 -*-
from odoo import http

# class MethodMejoraConciliacion(http.Controller):
#     @http.route('/method_mejora_conciliacion/method_mejora_conciliacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_mejora_conciliacion/method_mejora_conciliacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_mejora_conciliacion.listing', {
#             'root': '/method_mejora_conciliacion/method_mejora_conciliacion',
#             'objects': http.request.env['method_mejora_conciliacion.method_mejora_conciliacion'].search([]),
#         })

#     @http.route('/method_mejora_conciliacion/method_mejora_conciliacion/objects/<model("method_mejora_conciliacion.method_mejora_conciliacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_mejora_conciliacion.object', {
#             'object': obj
#         })