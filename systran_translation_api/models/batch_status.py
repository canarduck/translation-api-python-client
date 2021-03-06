#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


class BatchStatus(object):
    """
    NOTE: This class is auto generated by the systran code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        """
        Systran model

        :param dict systran_types: The key is attribute name and the value is attribute type.
        :param dict attribute_map: The key is attribute name and the value is json key in definition.
        """
        self.systran_types = {
            'cancelled': 'bool',
            'closed': 'bool',
            'created_at': 'float',
            'expire_at': 'float',
            'finished_at': 'float',
            'requests': 'list[BatchRequest]',
            'error': 'ErrorResponse'
        }

        self.attribute_map = {
            'cancelled': 'cancelled',
            'closed': 'closed',
            'created_at': 'createdAt',
            'expire_at': 'expireAt',
            'finished_at': 'finishedAt',
            'requests': 'requests',
            'error': 'error'
        }
        
        # Is the batch cancelled
        self.cancelled = None  # bool
        
        # Is the batch closed
        self.closed = None  # bool
        
        # Creation time of the batch (ms since the Epoch)
        self.created_at = None  # float
        
        # Expiration time of the batch (ms since the Epoch). Is null while there are pending requests
        self.expire_at = None  # float
        
        # Completion time of the batch (ms since the Epoch)
        self.finished_at = None  # float
        
        # Array of requests
        self.requests = None  # list[BatchRequest]
        
        # Error of the request
        self.error = None  # ErrorResponse
        

    def __repr__(self):
        properties = []
        for p in self.__dict__:
            if p != 'systran_types' and p != 'attribute_map':
                properties.append('{prop}={val!r}'.format(prop=p, val=self.__dict__[p]))

        return '<{name} {props}>'.format(name=__name__, props=' '.join(properties))


