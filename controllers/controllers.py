# -*- coding: utf-8 -*-
# from odoo import http


# class FleetLogs(http.Controller):
#     @http.route('/fleet_logs/fleet_logs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_logs/fleet_logs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_logs.listing', {
#             'root': '/fleet_logs/fleet_logs',
#             'objects': http.request.env['fleet_logs.fleet_logs'].search([]),
#         })

#     @http.route('/fleet_logs/fleet_logs/objects/<model("fleet_logs.fleet_logs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_logs.object', {
#             'object': obj
#         })
