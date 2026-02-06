import json
import os

from decouple import config

MAX_REPO = 70
SOURCE_REPO = "stacks-network/stacks-core"
run_number = os.environ.get('GITHUB_RUN_NUMBER', '0')


def get_cyclic_index(run_number, max_index=100):
    """Convert run number to a cyclic index between 1 and max_index"""
    return (int(run_number) - 1) % max_index + 1


if run_number == "0":
    BASE_URL = f"https://deepwiki.com/{SOURCE_REPO}"
else:
    # Convert to cyclic index (1-100)
    run_index = get_cyclic_index(run_number, MAX_REPO)
    # Format the URL with leading zeros
    repo_number = f"{run_index:03d}"
    BASE_URL = f"https://deepwiki.com/grass-dev-pa/stacks-core-{repo_number}"

scope_files = [
    'stacks-core/stacks-common/build.rs',
    'stacks-core/stacks-common/src/address/b58.rs',
    'stacks-core/stacks-common/src/address/c32.rs',
    'stacks-core/stacks-common/src/address/c32_old.rs',
    'stacks-core/stacks-common/src/address/mod.rs',
    'stacks-core/stacks-common/src/bitvec.rs',
    'stacks-core/stacks-common/src/codec/macros.rs',
    'stacks-core/stacks-common/src/codec/mod.rs',
    'stacks-core/stacks-common/src/deps_common/bech32/mod.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/block.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/constants.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/mod.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/opcodes.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/script.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/blockdata/transaction.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/internal_macros.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/mod.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/address.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/constants.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/encodable.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/message.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/message_blockdata.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/message_network.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/mod.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/network/serialize.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/util/hash.rs',
    'stacks-core/stacks-common/src/deps_common/bitcoin/util/mod.rs',
    'stacks-core/stacks-common/src/deps_common/ctrlc/error.rs',
    'stacks-core/stacks-common/src/deps_common/ctrlc/mod.rs',
    'stacks-core/stacks-common/src/deps_common/ctrlc/platform/mod.rs',
    'stacks-core/stacks-common/src/deps_common/ctrlc/platform/unix/mod.rs',
    'stacks-core/stacks-common/src/deps_common/ctrlc/platform/windows/mod.rs',
    'stacks-core/stacks-common/src/deps_common/httparse/mod.rs',
    'stacks-core/stacks-common/src/deps_common/httparse_tests/mod.rs',
    'stacks-core/stacks-common/src/deps_common/mod.rs',
    'stacks-core/stacks-common/src/libcommon.rs',
    'stacks-core/stacks-common/src/types/chainstate.rs',
    'stacks-core/stacks-common/src/types/mod.rs',
    'stacks-core/stacks-common/src/types/net.rs',
    'stacks-core/stacks-common/src/types/sqlite.rs',
    'stacks-core/stacks-common/src/util/chunked_encoding.rs',
    'stacks-core/stacks-common/src/util/db.rs',
    'stacks-core/stacks-common/src/util/hash.rs',
    'stacks-core/stacks-common/src/util/log.rs',
    'stacks-core/stacks-common/src/util/lru_cache.rs',
    'stacks-core/stacks-common/src/util/macros.rs',
    'stacks-core/stacks-common/src/util/mod.rs',
    'stacks-core/stacks-common/src/util/pair.rs',
    'stacks-core/stacks-common/src/util/pipe.rs',
    'stacks-core/stacks-common/src/util/retry.rs',
    'stacks-core/stacks-common/src/util/secp256k1/mod.rs',
    'stacks-core/stacks-common/src/util/secp256k1/native.rs',
    'stacks-core/stacks-common/src/util/secp256k1/wasm.rs',
    'stacks-core/stacks-common/src/util/secp256r1.rs',
    'stacks-core/stacks-common/src/util/serde_serializers.rs',
    'stacks-core/stacks-common/src/util/uint.rs',
    'stacks-core/stacks-common/src/util/vrf.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/address.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/bits.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/blocks.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/indexer.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/keys.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/messages.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/mod.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/network.rs',
    'stacks-core/stackslib/src/burnchains/bitcoin/spv.rs',
    'stacks-core/stackslib/src/burnchains/burnchain.rs',
    'stacks-core/stackslib/src/burnchains/db.rs',
    'stacks-core/stackslib/src/burnchains/indexer.rs',
    'stacks-core/stackslib/src/burnchains/mod.rs',
    'stacks-core/stackslib/src/chainstate/burn/atc.rs',
    'stacks-core/stackslib/src/chainstate/burn/db/mod.rs',
    'stacks-core/stackslib/src/chainstate/burn/db/processing.rs',
    'stacks-core/stackslib/src/chainstate/burn/db/sortdb.rs',
    'stacks-core/stackslib/src/chainstate/burn/distribution.rs',
    'stacks-core/stackslib/src/chainstate/burn/mod.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/delegate_stx.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/leader_block_commit.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/leader_key_register.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/mod.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/stack_stx.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/transfer_stx.rs',
    'stacks-core/stackslib/src/chainstate/burn/operations/vote_for_aggregate_key.rs',
    'stacks-core/stackslib/src/chainstate/burn/sortition.rs',
    'stacks-core/stackslib/src/chainstate/coordinator/comm.rs',
    'stacks-core/stackslib/src/chainstate/coordinator/mod.rs',
    'stacks-core/stackslib/src/chainstate/mod.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/coordinator/mod.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/keys.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/miner.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/mod.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/shadow.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/signer_set.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/staging_blocks.rs',
    'stacks-core/stackslib/src/chainstate/nakamoto/tenure.rs',
    'stacks-core/stackslib/src/chainstate/stacks/address.rs',
    'stacks-core/stackslib/src/chainstate/stacks/auth.rs',
    'stacks-core/stackslib/src/chainstate/stacks/block.rs',
    'stacks-core/stackslib/src/chainstate/stacks/boot/bns.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/cost-voting.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/costs-2-testnet.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/costs-2.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/costs-3.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/costs-4.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/costs.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/docs.rs',
    'stacks-core/stackslib/src/chainstate/stacks/boot/genesis.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/lockup.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/mod.rs',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox-2.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox-3.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox-4.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox-mainnet.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox-testnet.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/pox.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/signers-0-xxx.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/signers-1-xxx.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/signers-voting.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/signers.clar',
    'stacks-core/stackslib/src/chainstate/stacks/boot/sip-031.clar',
    'stacks-core/stackslib/src/chainstate/stacks/db/accounts.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/blocks.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/contracts.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/headers.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/mod.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/transactions.rs',
    'stacks-core/stackslib/src/chainstate/stacks/db/unconfirmed.rs',
    'stacks-core/stackslib/src/chainstate/stacks/events.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/bits.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/cache.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/file.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/marf.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/mod.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/node.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/profile.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/proofs.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/storage.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/trie.rs',
    'stacks-core/stackslib/src/chainstate/stacks/index/trie_sql.rs',
    'stacks-core/stackslib/src/chainstate/stacks/miner.rs',
    'stacks-core/stackslib/src/chainstate/stacks/mod.rs',
    'stacks-core/stackslib/src/chainstate/stacks/transaction.rs',
    'stacks-core/stackslib/src/clarity_vm/clarity.rs',
    'stacks-core/stackslib/src/clarity_vm/database/ephemeral.rs',
    'stacks-core/stackslib/src/clarity_vm/database/marf.rs',
    'stacks-core/stackslib/src/clarity_vm/database/mod.rs',
    'stacks-core/stackslib/src/clarity_vm/mod.rs',
    'stacks-core/stackslib/src/clarity_vm/special.rs',
    'stacks-core/stackslib/src/config/chain_data.rs',
    'stacks-core/stackslib/src/config/mod.rs',
    'stacks-core/stackslib/src/core/mempool.rs',
    'stacks-core/stackslib/src/core/mod.rs',
    'stacks-core/stackslib/src/core/nonce_cache.rs',
    'stacks-core/stackslib/src/cost_estimates/fee_medians.rs',
    'stacks-core/stackslib/src/cost_estimates/fee_rate_fuzzer.rs',
    'stacks-core/stackslib/src/cost_estimates/fee_scalar.rs',
    'stacks-core/stackslib/src/cost_estimates/metrics.rs',
    'stacks-core/stackslib/src/cost_estimates/mod.rs',
    'stacks-core/stackslib/src/cost_estimates/pessimistic.rs',
    'stacks-core/stackslib/src/deps/mod.rs',
    'stacks-core/stackslib/src/lib.rs',
    'stacks-core/stackslib/src/monitoring/mod.rs',
    'stacks-core/stackslib/src/monitoring/prometheus.rs',
    'stacks-core/stackslib/src/net/api/blockreplay.rs',
    'stacks-core/stackslib/src/net/api/blocksimulate.rs',
    'stacks-core/stackslib/src/net/api/callreadonly.rs',
    'stacks-core/stackslib/src/net/api/fastcallreadonly.rs',
    'stacks-core/stackslib/src/net/api/get_tenure_tip_meta.rs',
    'stacks-core/stackslib/src/net/api/get_tenures_fork_info.rs',
    'stacks-core/stackslib/src/net/api/getaccount.rs',
    'stacks-core/stackslib/src/net/api/getattachment.rs',
    'stacks-core/stackslib/src/net/api/getattachmentsinv.rs',
    'stacks-core/stackslib/src/net/api/getblock.rs',
    'stacks-core/stackslib/src/net/api/getblock_v3.rs',
    'stacks-core/stackslib/src/net/api/getblockbyheight.rs',
    'stacks-core/stackslib/src/net/api/getclaritymarfvalue.rs',
    'stacks-core/stackslib/src/net/api/getclaritymetadata.rs',
    'stacks-core/stackslib/src/net/api/getconstantval.rs',
    'stacks-core/stackslib/src/net/api/getcontractabi.rs',
    'stacks-core/stackslib/src/net/api/getcontractsrc.rs',
    'stacks-core/stackslib/src/net/api/getdatavar.rs',
    'stacks-core/stackslib/src/net/api/getheaders.rs',
    'stacks-core/stackslib/src/net/api/gethealth.rs',
    'stacks-core/stackslib/src/net/api/getinfo.rs',
    'stacks-core/stackslib/src/net/api/getistraitimplemented.rs',
    'stacks-core/stackslib/src/net/api/getmapentry.rs',
    'stacks-core/stackslib/src/net/api/getmicroblocks_confirmed.rs',
    'stacks-core/stackslib/src/net/api/getmicroblocks_indexed.rs',
    'stacks-core/stackslib/src/net/api/getmicroblocks_unconfirmed.rs',
    'stacks-core/stackslib/src/net/api/getneighbors.rs',
    'stacks-core/stackslib/src/net/api/getpoxinfo.rs',
    'stacks-core/stackslib/src/net/api/getsigner.rs',
    'stacks-core/stackslib/src/net/api/getsortition.rs',
    'stacks-core/stackslib/src/net/api/getstackerdbchunk.rs',
    'stacks-core/stackslib/src/net/api/getstackerdbmetadata.rs',
    'stacks-core/stackslib/src/net/api/getstackers.rs',
    'stacks-core/stackslib/src/net/api/getstxtransfercost.rs',
    'stacks-core/stackslib/src/net/api/gettenure.rs',
    'stacks-core/stackslib/src/net/api/gettenureblocks.rs',
    'stacks-core/stackslib/src/net/api/gettenureblocksbyhash.rs',
    'stacks-core/stackslib/src/net/api/gettenureblocksbyheight.rs',
    'stacks-core/stackslib/src/net/api/gettenureinfo.rs',
    'stacks-core/stackslib/src/net/api/gettenuretip.rs',
    'stacks-core/stackslib/src/net/api/gettransaction.rs',
    'stacks-core/stackslib/src/net/api/gettransaction_unconfirmed.rs',
    'stacks-core/stackslib/src/net/api/liststackerdbreplicas.rs',
    'stacks-core/stackslib/src/net/api/mod.rs',
    'stacks-core/stackslib/src/net/api/postblock.rs',
    'stacks-core/stackslib/src/net/api/postblock_proposal.rs',
    'stacks-core/stackslib/src/net/api/postblock_v3.rs',
    'stacks-core/stackslib/src/net/api/postfeerate.rs',
    'stacks-core/stackslib/src/net/api/postmempoolquery.rs',
    'stacks-core/stackslib/src/net/api/postmicroblock.rs',
    'stacks-core/stackslib/src/net/api/poststackerdbchunk.rs',
    'stacks-core/stackslib/src/net/api/posttransaction.rs',
    'stacks-core/stackslib/src/net/asn.rs',
    'stacks-core/stackslib/src/net/atlas/db.rs',
    'stacks-core/stackslib/src/net/atlas/download.rs',
    'stacks-core/stackslib/src/net/atlas/mod.rs',
    'stacks-core/stackslib/src/net/chat.rs',
    'stacks-core/stackslib/src/net/codec.rs',
    'stacks-core/stackslib/src/net/connection.rs',
    'stacks-core/stackslib/src/net/db.rs',
    'stacks-core/stackslib/src/net/dns.rs',
    'stacks-core/stackslib/src/net/download/epoch2x.rs',
    'stacks-core/stackslib/src/net/download/mod.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/download_state_machine.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/mod.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/tenure.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/tenure_downloader.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/tenure_downloader_set.rs',
    'stacks-core/stackslib/src/net/download/nakamoto/tenure_downloader_unconfirmed.rs',
    'stacks-core/stackslib/src/net/http/common.rs',
    'stacks-core/stackslib/src/net/http/error.rs',
    'stacks-core/stackslib/src/net/http/mod.rs',
    'stacks-core/stackslib/src/net/http/request.rs',
    'stacks-core/stackslib/src/net/http/response.rs',
    'stacks-core/stackslib/src/net/http/stream.rs',
    'stacks-core/stackslib/src/net/httpcore.rs',
    'stacks-core/stackslib/src/net/inv/epoch2x.rs',
    'stacks-core/stackslib/src/net/inv/mod.rs',
    'stacks-core/stackslib/src/net/inv/nakamoto.rs',
    'stacks-core/stackslib/src/net/mempool/mod.rs',
    'stacks-core/stackslib/src/net/mod.rs',
    'stacks-core/stackslib/src/net/neighbors/comms.rs',
    'stacks-core/stackslib/src/net/neighbors/db.rs',
    'stacks-core/stackslib/src/net/neighbors/mod.rs',
    'stacks-core/stackslib/src/net/neighbors/neighbor.rs',
    'stacks-core/stackslib/src/net/neighbors/rpc.rs',
    'stacks-core/stackslib/src/net/neighbors/walk.rs',
    'stacks-core/stackslib/src/net/p2p.rs',
    'stacks-core/stackslib/src/net/poll.rs',
    'stacks-core/stackslib/src/net/prune.rs',
    'stacks-core/stackslib/src/net/relay.rs',
    'stacks-core/stackslib/src/net/rpc.rs',
    'stacks-core/stackslib/src/net/server.rs',
    'stacks-core/stackslib/src/net/stackerdb/config.rs',
    'stacks-core/stackslib/src/net/stackerdb/db.rs',
    'stacks-core/stackslib/src/net/stackerdb/mod.rs',
    'stacks-core/stackslib/src/net/stackerdb/sync.rs',
    'stacks-core/stackslib/src/net/unsolicited.rs',
    'stacks-core/stackslib/src/proptest_utils.rs',
    'stacks-core/stackslib/src/util_lib/bloom.rs',
    'stacks-core/stackslib/src/util_lib/boot.rs',
    'stacks-core/stackslib/src/util_lib/db.rs',
    'stacks-core/stackslib/src/util_lib/mod.rs',
    'stacks-core/stackslib/src/util_lib/signed_structured_data.rs',
    'stacks-core/stackslib/src/util_lib/strings.rs',
    'stacks-core/stacks-node/src/burnchains/bitcoin/core_controller.rs',
    'stacks-core/stacks-node/src/burnchains/bitcoin/mod.rs',
    'stacks-core/stacks-node/src/burnchains/bitcoin_regtest_controller.rs',
    'stacks-core/stacks-node/src/burnchains/mocknet_controller.rs',
    'stacks-core/stacks-node/src/burnchains/mod.rs',
    'stacks-core/stacks-node/src/burnchains/rpc/bitcoin_rpc_client/mod.rs',
    'stacks-core/stacks-node/src/burnchains/rpc/mod.rs',
    'stacks-core/stacks-node/src/burnchains/rpc/rpc_transport/mod.rs',
    'stacks-core/stacks-node/src/event_dispatcher.rs',
    'stacks-core/stacks-node/src/event_dispatcher/db.rs',
    'stacks-core/stacks-node/src/event_dispatcher/payloads.rs',
    'stacks-core/stacks-node/src/event_dispatcher/stacker_db.rs',
    'stacks-core/stacks-node/src/genesis_data.rs',
    'stacks-core/stacks-node/src/globals.rs',
    'stacks-core/stacks-node/src/keychain.rs',
    'stacks-core/stacks-node/src/main.rs',
    'stacks-core/stacks-node/src/monitoring/mod.rs',
    'stacks-core/stacks-node/src/monitoring/prometheus.rs',
    'stacks-core/stacks-node/src/nakamoto_node.rs',
    'stacks-core/stacks-node/src/nakamoto_node/miner.rs',
    'stacks-core/stacks-node/src/nakamoto_node/miner_db.rs',
    'stacks-core/stacks-node/src/nakamoto_node/peer.rs',
    'stacks-core/stacks-node/src/nakamoto_node/relayer.rs',
    'stacks-core/stacks-node/src/nakamoto_node/signer_coordinator.rs',
    'stacks-core/stacks-node/src/nakamoto_node/stackerdb_listener.rs',
    'stacks-core/stacks-node/src/neon_node.rs',
    'stacks-core/stacks-node/src/node.rs',
    'stacks-core/stacks-node/src/operations.rs',
    'stacks-core/stacks-node/src/run_loop/boot_nakamoto.rs',
    'stacks-core/stacks-node/src/run_loop/helium.rs',
    'stacks-core/stacks-node/src/run_loop/mod.rs',
    'stacks-core/stacks-node/src/run_loop/nakamoto.rs',
    'stacks-core/stacks-node/src/run_loop/neon.rs',
    'stacks-core/stacks-node/src/syncctl.rs',
    'stacks-core/stacks-node/src/tenure.rs',
]



def question_generator(target_file: str) -> str:
    """
    Generates targeted security audit questions for a specific stacks-core file.

    Args:
        target_file: The specific file path to focus question generation on
                     (e.g., "stacks-core/stackslib/src/chainstate/stacks/block.rs")

    Returns:
        A formatted prompt string for generating security questions
    """
    prompt = f"""
# Generate Targeted Security Audit Questions for Stacks Core Protocol

## Context

The target project is **stacks-core**, the Rust reference implementation of the
Stacks blockchain. Stacks is a Bitcoin-anchored L2 that uses **Proof of Transfer (PoX)**
for leader election and security anchoring, and provides deterministic smart
contracts via the **Clarity VM**. The codebase implements Stacks block/transaction
processing, chainstate and state indexing (MARF), burnchain interaction with
Bitcoin, microblocks, mempool policies, RPC/P2P handling, and consensus-critical
validation rules. Core cryptography includes secp256k1 signatures, VRF proofs,
hashing, and address encoding/decoding. The system enforces protocol invariants
around PoX reward cycles, tenure changes, block cost limits, transaction validity,
and Clarity execution semantics.

## Scope

CRITICAL TARGET FILE: Focus question generation **exclusively** on `{target_file}`.
All questions must reference logic that exists in `{target_file}` only.

If you cannot generate enough questions from this single file, provide as many
high-quality questions as the file's complexity allows. Do not return empty results.

Target file should be within the audit scope:
- stacks-core/stacks-common
- stacks-core/stackslib
- stacks-core/stacks-node/src

## Core Components (reference only)

This list is for context; do not generate questions about other files.

core_components = [
    "stacks-common/src/address",           # C32 address encoding/decoding
    "stacks-common/src/util",              # Hashing, secp256k1, VRF utilities
    "stackslib/src/chainstate",            # Blocks, transactions, state transitions
    "stackslib/src/burnchains",            # Bitcoin burnchain interaction, sortition
    "stackslib/src/clarity_vm",            # Clarity VM execution and cost model
    "stackslib/src/net",                   # P2P, RPC, and network message handling
    "stackslib/src/mempool",               # Transaction admission and policy
    "stackslib/src/chainstate/stacks/boot",# Consensus-critical Clarity boot contracts
    "stacks-node/src/run_loop",            # Node startup, block processing loop
    "stacks-node/src/neon",                # Node runtime and consensus wiring
]

## Stacks Architecture & Security Layers

1) PoX + Burnchain Anchoring
   - Bitcoin block commits determine leader election and tenure
   - Sortition, VRF proofs, and burnchain consensus hashes bind Stacks blocks
   - Reward cycles, stacking lockups, and miner rewards are consensus-critical

2) Stacks Chainstate and Consensus
   - Stacks blocks, microblocks, tenure changes, and fork choice rules
   - Chainstate indexing (MARF) and state root / trie hash invariants
   - Block size and execution cost limits

3) Clarity Smart Contracts
   - Deterministic execution and strict cost accounting
   - AST prechecks and type system invariants
   - Post-conditions, asset balance changes, and contract-call semantics

4) Transaction Validation
   - Nonce handling, fee rules, signature checks, and network/version fields
   - Serialization and deserialization of consensus-critical data
   - Rejecting invalid or malformed inputs and preventing replay/double-spend

5) Networking and Mempool Policies
   - Safe parsing of untrusted data
   - Mempool admission rules consistent with consensus
   - DoS resistance in validation and batch processing

## Critical Security Invariants

- Canonical chain selection must be deterministic and consensus-safe
- Stacks block headers must correctly bind to burnchain/VRF data
- Microblocks must only be accepted from the current tenure leader
- Execution cost accounting must never under-charge or overflow
- Transaction nonces must be strictly enforced per account
- Signature verification must reject malformed keys, signatures, and hashes
- PoX lockups/reward cycles must be enforced without off-by-one errors
- MARF/state root hashes must match the validated chainstate
- Clarity post-conditions must match actual state changes
- Serialization must be deterministic and reject ambiguous encodings

## In-Scope Vulnerability Categories

Critical:
- Consensus divergence, chain fork inconsistencies, or state root mismatch
- Unauthorized fund movement or STX balance corruption
- Signature verification bypass or forgery
- PoX reward theft or incorrect reward distribution
- Contract execution rule bypass leading to invalid state transitions

High:
- Denial of service via expensive validation or malformed inputs
- Transaction malleability or replay that changes consensus outcomes
- Cost accounting bypass or underestimation
- Mempool policy inconsistencies that allow invalid blocks

Medium:
- Incorrect error handling leading to rejected valid blocks/txs
- Parsing edge cases that accept invalid data
- Non-consensus state corruption or data loss

## Goals for Question Generation

- Focus on mathematical correctness, protocol business logic, and invariants
- Require concrete attack paths and preconditions
- Tie each question to a specific function, struct, or logic block in `{target_file}`
- Prioritize consensus-critical issues and high-severity impacts
- Avoid out-of-scope issues (UI, social engineering, non-protocol concerns)
- For Clarity `.clar` files, reference `define-public`, `define-private`,
  `define-read-only`, and their state transitions

## Question Format Template

Each question must follow this Python list format:

questions = [
    "[File: {target_file}] [Function: function_name()] [Vulnerability Type] Specific question describing the attack vector, preconditions, invariant violated, and impact? (Severity)",
]

## Target Question Count

- Large files (>1000 lines): aim for 150-300 questions
- Medium files (500-1000 lines): aim for 80-150 questions
- Smaller files (<500 lines): aim for 30-80 questions
- If the file is smaller or narrow in scope, generate as many high-quality
  questions as the logic supports; do not include filler questions

Begin generating questions for `{target_file}` now.
"""
    return prompt

def question_format(security_question: str) -> str:
    """
    Generate a comprehensive security audit prompt for stacks-core.

    Args:
        security_question: The specific security concern to investigate

    Returns:
        A detailed audit prompt with validation requirements
    """
    prompt = f"""# STACKS-CORE SECURITY AUDIT PROMPT

## Security Question to Investigate:
{security_question}

## Codebase Context

You are auditing **stacks-core**, the Rust reference implementation of the
Stacks blockchain. Stacks is a Bitcoin-anchored L2 that uses **Proof of Transfer (PoX)**
for leader election and security anchoring, and uses the **Clarity VM** for
deterministic smart contracts. The system enforces consensus-critical rules
around burnchain sortition, VRF proofs, block and microblock processing,
transaction validation, execution cost limits, and chainstate indexing (MARF).

### Core Components (reference only)
- stacks-common: address encoding, hashing, secp256k1, VRF utilities
- stackslib: chainstate, burnchain, consensus logic, MARF, Clarity VM
- stacks-node/src: node run loop, P2P/RPC, block processing, mempool

## CRITICAL INVARIANTS (Must Hold at All Times)

1) **Consensus Determinism**: All nodes must process the same block/tx and
   produce identical state roots and consensus outcomes.
2) **Burnchain Anchoring**: Stacks block headers must correctly bind to the
   burnchain header hash, consensus hash, and VRF proof where required.
3) **Tenure and Microblock Rules**: Only the current tenure leader can issue
   microblocks; tenure changes must be consistent with sortition results.
4) **Execution Cost Accounting**: Clarity execution costs must not underflow,
   overflow, or be bypassed; limits must be enforced per block and per tx.
5) **Transaction Validity**: Nonces, signatures, fees, and post-conditions must
   be strictly enforced without off-by-one or serialization ambiguities.
6) **PoX Reward Cycle Logic**: Reward cycles, lockups, and reward distribution
   must be correct and not susceptible to manipulation.
7) **State Root Integrity**: MARF and state root hashes must match the validated
   chainstate for each block and microblock stream.

## ATTACK SURFACES TO CONSIDER

1) **Block and Microblock Validation**
   - header validation, burnchain/VRF binding, chain continuity
   - microblock acceptance rules, stream ordering, tenure change boundaries

2) **Transaction Processing**
   - nonce and signature checks, fees, post-conditions
   - serialization/deserialization and canonical encoding

3) **Clarity VM and Smart Contracts**
   - cost model correctness, AST precheck rules, type safety
   - on-chain boot contracts and reward logic invariants

4) **Burnchain + PoX**
   - sortition, reward cycles, stacking lockups, miner rewards
   - cross-chain data consistency and replay resistance

5) **Networking and Mempool**
   - parsing of untrusted data, resource exhaustion, mempool vs consensus
   - RPC/P2P reachable attack paths only

## IN-SCOPE VULNERABILITY SEVERITY (Must Use These Definitions)

Critical:
- Any network shutdown or inability to confirm new valid transactions for multiple blocks
- Any deep fork of 10+ blocks without the requisite Bitcoin spend
- Any direct loss of funds (excluding freezing)
- Any chain split caused by nodes processing the same block/tx differently
- Any confirmation of an invalid transaction (e.g., incorrect nonce)

High:
- Any unintended chain split or network partition
- Any remotely exploitable memory access, disk access, or persistent code execution
  (attacks restricted to RPC/P2P ports only)

Medium:
- Any transient consensus failures

Low:
- Any remotely exploitable denial of service in a node
- Any network DoS impacting >10% of miners that does not shut down the network

## VULNERABILITY VALIDATION REQUIREMENTS

A finding is ONLY valid if it passes ALL of these checks:

### Impact Assessment (Concrete and Measurable)
- What exact invariant is broken?
- What is the concrete harm (consensus failure, funds loss, invalid tx acceptance)?
- Quantify the impact where possible (blocks, funds, affected nodes).

### Likelihood Assessment (Practical and Realistic)
- What attacker capabilities are required?
- Can the attack be executed via RPC/P2P only when required?
- Are the costs and resources realistic relative to impact?
- Can the attack succeed without breaking cryptographic primitives?

### Validation Checklist
1) Code location identified: exact file/function/line(s)
2) Root cause analysis: why the bug exists
3) Exploitation path: step-by-step trigger
4) Realistic parameters and prerequisites
5) Proof of concept or detailed exploit algorithm
6) Impact and severity mapped to the scope above
7) Existing mitigations verified and shown insufficient

## AUDIT REPORT FORMAT

If a valid vulnerability is found (after passing all validation checks), provide
a report in this exact format:

### Title
[Concise, descriptive title]

### Summary
[2-3 sentence executive summary of the vulnerability and impact]

### Finding Description
[Technical description with code location, root cause, and relevant context]

### Impact Explanation
[Concrete impact assessment with severity and affected components]

### Likelihood Explanation
[Realistic exploitation analysis with prerequisites and feasibility]

### Recommendation
[Specific, actionable fix and tests]

### Proof of Concept
[Exploit steps or code, with realistic parameters and expected behavior]

## STRICT OUTPUT REQUIREMENT

IF you find a vulnerability that passes all validation checks:
-> Output the complete audit report in the format above

IF no valid vulnerability exists:
-> Output exactly: "#NoVulnerability found for this question."

Do not output anything else. Be skeptical and do not speculate.

Begin your investigation of: {security_question}
"""
    return prompt



def validation_format(report: str) -> str:
    """
    Generates a comprehensive validation prompt for stacks-core security claims.

    Args:
        report: A security vulnerability report to validate

    Returns:
        A formatted validation prompt string for strict technical scrutiny
    """
    prompt = f"""
You are an Elite Stacks Core Security Judge with deep expertise in the Stacks
blockchain protocol, Proof of Transfer (PoX), burnchain anchoring, Clarity VM,
chainstate (MARF) invariants, and consensus-critical transaction validation.
Your ONLY task is ruthless technical validation of security claims against the
stacks-core codebase.

Note: Stacks core developers and node operators are trusted roles.

SECURITY CLAIM TO VALIDATE:
{report}

================================================================================
## STACKS-CORE VALIDATION FRAMEWORK

### PHASE 1: IMMEDIATE DISQUALIFICATION CHECKS
Reject immediately (#NoVulnerability) if ANY apply:

Note before a vulnerability can be considered valid it must have a valid impact
and also a valid likelihood that can be triggered or trigger validly on its own.
If a vulnerability cannot be triggered then it is invalid, except there is a
logic vulnerability. This is very important.

And your return must either be the report or #NoVulnerability because this is
automated and that is the only way I can understand.

Note this is the most important: any vulnerability with no valid impact to the
protocol is invalid. Any vulnerability that requires a user to deploy a Clarity
contract and only self-harm users is invalid because it does not affect the
protocol. This is normal behavior because the blockchain is a dark forest.

Note before a vulnerability can be considered valid it must have a valid impact
and also a valid likelihood that can be triggered or trigger validly on its own.
If a vulnerability cannot be triggered then it is invalid, except there is a
logic vulnerability. This is very important.

And your return must either be the report or #NoVulnerability because this is
automated and that is the only way I can understand.

#### A. Scope Violations
- Affects files not in stacks-core production codebase
- Targets any file under test directories (tests/, test/, testing/, fuzz/)
- Claims about documentation, comments, code style, or logging
- Focuses on external tools or dev-only utilities outside runtime behavior

In-Scope Components:
- stacks-core/stacks-common (address encoding, hashing, secp256k1, VRF utils)
- stacks-core/stackslib (chainstate, burnchain, Clarity VM, MARF, consensus)
- stacks-core/stacks-node/src (node run loop, RPC/P2P, block processing)

Verify: every file path cited in the report matches the stacks-core source
structure above and is not a test or fuzz file.

#### B. Threat Model Violations
- Requires compromised Stacks core developers or node administrators
- Assumes breaking cryptographic primitives (secp256k1, SHA-256, VRF)
- Depends on social engineering, phishing, or private key theft
- Relies on infrastructure attacks (BGP hijacking, DNS poisoning, volumetric DDoS)
- Requires non-RPC/P2P access when the scope requires remote exploitability

Trusted Roles: Stacks core developers and node operators.
Untrusted Actors: transaction submitters, miners, stackers, RPC clients, P2P peers.

#### C. Known Issues / Exclusions
- Any finding already documented in public advisories or fixed releases
- Issues in external dependencies unless the report proves impact on stacks-core
- Performance optimizations without security impact
- Non-consensus configuration mistakes or misconfigurations by operators

#### D. Non-Security Issues
- Code style, naming conventions, refactoring suggestions
- Missing logs/events without security impact
- Documentation issues or TODOs
- Minor precision errors with negligible impact
- Theoretical issues without a concrete exploit path

#### E. Invalid Exploit Scenarios
- Requires inputs that cannot be delivered through RPC/P2P message formats
- Depends on invalid blocks or transactions without showing a validation bypass
- Relies on internal-only functions not reachable from protocol entry points
- Assumes unrealistic timing outside the protocol rules
- Requires breaking Bitcoin consensus to achieve the claimed impact

### PHASE 2: STACKS-SPECIFIC DEEP CODE VALIDATION
#### Step 1: Trace Complete Execution Path Through Stacks Architecture
Stacks Flow Patterns:
1) Transaction Flow: RPC/P2P submission -> mempool admission -> block assembly
   -> Clarity execution -> chainstate commit -> MARF/state root update
2) Burnchain/PoX Flow: Bitcoin block commit -> sortition -> tenure change
   -> Stacks block acceptance -> microblock stream validation
3) Clarity Flow: AST precheck -> type checking -> cost accounting -> execution
   -> post-conditions -> state transition

For each claim, reconstruct the full execution path:
1) Identify entry point: RPC endpoint, P2P message, or block/tx processing path
2) Trace internal calls and data flow
3) Document state before exploit (balances, nonces, tenure, reward cycle)
4) Enumerate state transitions and invariant checks
5) Verify protections and whether they can be bypassed
6) Show final incorrect state or consensus divergence

#### Step 2: Validate Every Claim With Code Evidence
Required Evidence:
- Exact file path and line numbers
- Direct code quotes showing the vulnerable logic
- Call traces with concrete parameter values
- Explicit invariant violation tied to Stacks consensus rules

Red Flags (indicate INVALID):
1) Missing Validation claims without showing bypass of all checks
2) PoX or reward cycle manipulation claims without showing the exact rule break
3) Microblock/tenure attacks without showing leader authorization bypass
4) Chain split claims without demonstrating deterministic divergence
5) Invalid transaction acceptance claims without showing how validation is bypassed

#### Step 3: Cross-Reference With Known Stacks Issues
1) Confirm the issue is not already fixed in current release branches
2) Check if tests or protocol rules would already catch the issue
3) Ensure the report matches current mainnet behavior

### PHASE 3: IMPACT AND EXPLOITABILITY VALIDATION (STACKS SCOPE)
Impact must be concrete and match these categories:

Critical:
- Any network shutdown or inability to confirm new valid transactions for multiple blocks
- Any triggering of a deep fork of 10 or more blocks without spending the requisite Bitcoin
- Any direct loss of funds other than through freezing
- Any chain split caused by nodes processing the same block/tx differently
- Any confirmation of an invalid transaction (such as incorrect nonce)

High:
- Any unintended chain split or network partition
- Any remotely exploitable memory access, disk access, or persistent code execution
  (attacks restricted to Stacks RPC/P2P ports)

Medium:
- Any transient consensus failures

Low:
- Any remotely exploitable denial of service in a node
- Any network denial of service impacting more than 10 percent of miners that
  does not shut down the network

Invalid Impacts (out of scope):
- Purely theoretical issues without exploitability
- Issues that only affect a single self-deployed contract without protocol impact
- Operator misconfiguration or local-only failures

Likelihood Reality Check:
- Can the attack be executed with realistic inputs and resources?
- Are the prerequisites achievable by an untrusted actor?
- Does the exploit avoid breaking cryptography or consensus assumptions?
- If remote, is it reachable via RPC/P2P only?

### PHASE 4: FINAL VALIDATION CHECKLIST
Before accepting any vulnerability, verify:
1) Scope compliance: production code only, no tests or fuzz
2) Trust model: no reliance on trusted role compromise
3) Impact severity: matches the scope categories above
4) Technical feasibility: reproducible with realistic parameters
5) Protocol impact: breaks consensus, safety, or funds invariants
6) Proof of concept: concrete steps or code to demonstrate exploit
7) Not a known issue or already fixed

Remember: false positives harm credibility. Assume claims are invalid until
overwhelming evidence proves otherwise.

---

AUDIT REPORT FORMAT (if vulnerability found):

Audit Report

## Title
The Title Of the Report

## Summary
A short summary of the issue, keep it brief.

## Finding Description
A more detailed explanation of the issue. Poorly written or incorrect findings
may result in rejection and a decrease of reputation score.

Describe which security guarantees it breaks and how it breaks them. If this
bug does not automatically happen, show how a malicious input would propagate
through the system to the part of the code where the issue occurs.

## Impact Explanation
Elaborate on why you have chosen a particular impact assessment.

## Likelihood Explanation
Explain how likely this is to occur and why.

## Recommendation
How can the issue be fixed or solved. Preferably, you can also add a snippet of
the fixed code here.

## Proof of Concept
Note very important: the PoC must have a valid test that runs just one function
that proves the vulnerability.

Remember: false positives harm credibility more than missed findings. Assume
claims are invalid until overwhelming evidence proves otherwise.

Now perform STRICT validation of the claim above.

Output ONLY:
- A full audit report (if genuinely valid after passing all checks above)
- #NoVulnerability found for this question. (if any check fails)
- If you cannot validate the claim or do not understand, send #NoVulnerability
- Only show full report when you know this is actually and truly a valid vulnerability
"""
    return prompt

