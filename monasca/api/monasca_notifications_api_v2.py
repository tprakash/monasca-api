# Copyright 2014 Hewlett-Packard
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from monasca.common import resource_api
from monasca.openstack.common import log


LOG = log.getLogger(__name__)


class NotificationsV2API(object):

    def __init__(self, global_conf):
        LOG.debug('initializing V2API!')
        self.global_conf = global_conf

    @resource_api.Restify('/v2.0/notification-methods', method='post')
    def do_post_notification_methods(self, req, res):
        res.status = '501 Not Implemented'

    @resource_api.Restify('/v2.0/notification-methods/{id}', method='delete')
    def do_delete_notification_methods(self, req, res, id):
        res.status = '501 Not Implemented'

    @resource_api.Restify('/v2.0/notification-methods', method='get')
    def do_get_notification_methods(self, req, res):
        res.status = '501 Not Implemented'

    @resource_api.Restify('/v2.0/notification-methods/{id}', method='get')
    def do_get_notification_method(self, req, res, id):
        res.status = '501 Not Implemented'

    @resource_api.Restify('/v2.0/notification-methods/{id}', method='put')
    def do_put_notification_methods(self, req, res, id):
        res.status = '501 Not Implemented'
