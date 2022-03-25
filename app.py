#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk import Stack, aws_opensearchservice as opensearch
from constructs import Construct


class OpensearchStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prod_domain = opensearch.Domain(
            self,
            "Domain",
            version=opensearch.EngineVersion.OPENSEARCH_1_1,
            # enable_version_upgrade=True,
            capacity=opensearch.CapacityConfig(master_nodes=5, data_nodes=20),
            ebs=opensearch.EbsOptions(volume_size=20),
            zone_awareness=opensearch.ZoneAwarenessConfig(availability_zone_count=3),
            logging=opensearch.LoggingOptions(
                slow_search_log_enabled=True,
                app_log_enabled=True,
                slow_index_log_enabled=True,
            ),
        )


app = cdk.App()
OpensearchStack(app, "OpensearchStackWithoutEnableVersionUpgrade")
app.synth()
