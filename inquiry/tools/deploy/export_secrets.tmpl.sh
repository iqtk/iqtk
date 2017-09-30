#!/usr/bin/env bash
# Copyright 2017 The Regents of the University of California
#
# Licensed under the BSD-3-clause license (the "License"); you may not
# use this file except in compliance with the License.
# You are provided a copy of the license in LICENSE.md at the root of
# this project.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export IQTK_DEPLOY_PROJECT_ID=[your gcloud project ID]
export IQTK_API_KEY=[your gcloud API key]
export IQTK_OAUTH_CLIENT_ID=[your gcloud OAUTH client ID]
export IQTK_CLIENT_SECRETS_FILE=[local path to your gcloud OAUTH client secrets file]
export LOCAL_SA_KEY_JSON=[local path to your gcloud service account key]
