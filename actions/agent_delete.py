# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lib.actions import OrionBaseAction


class AgentDelete(OrionBaseAction):
    def run(self, node=None):
        """
        Delete Orion Agent
        """

        self.connect()

        orion_agent = self.get_agent(node)

        if not orion_agent:
            raise ValueError("Agent not found")

        orion_data = self.delete(orion_agent['Uri'])

        # This Delete always returns None, so check and return True
        if orion_data is None:
            return True
        else:
            return orion_data
