from __future__ import absolute_import

from collections import namedtuple


# Other useful structs
TopicPartition = namedtuple("TopicPartition",
    ["topic", "partition"])

BrokerMetadata = namedtuple("BrokerMetadata",
    ["nodeId", "host", "port", "rack"])

PartitionMetadata = namedtuple("PartitionMetadata",
    ["topic", "partition", "leader", "replicas", "isr", "error"])

OffsetAndMetadata = namedtuple("OffsetAndMetadata",
    # TODO add leaderEpoch: OffsetAndMetadata(offset, leaderEpoch, metadata)
    ["offset", "metadata"])

OffsetAndTimestamp = namedtuple("OffsetAndTimestamp",
    ["offset", "timestamp"])

MemberInformation = namedtuple("MemberInformation",
    ["member_id", "client_id", "client_host", "member_metadata", "member_assignment"])

GroupInformation = namedtuple("GroupInformation",
    ["error_code", "group", "state", "protocol_type", "protocol", "members", "authorized_operations"])

# Define retry policy for async producer
# Limit value: int >= 0, 0 means no retries
RetryOptions = namedtuple("RetryOptions",
    ["limit", "backoff_ms", "retry_on_timeouts"])
