# MONOLITHIC INSTRUCTION DAG (asm.md)

[SECTION: INIT_WORKSPACE]
DEPENDS : []
INPUTS  : ["specs/specs.md"]
OP      : mkdir -p .tmp/sandbox
OUT     : ".tmp/sandbox/.init_lock"
ASSERT  : [ -f .tmp/sandbox/.init_lock ]

[SECTION: PROCESS_PRIMARY_STREAM]
DEPENDS : [INIT_WORKSPACE]
INPUTS  : [".tmp/sandbox/.init_lock"]
OP      : <OPCODE_WITH_CLI_FLAGS>
OUT     : ".tmp/sandbox/primary_output.bin"
ASSERT  : [ -f .tmp/sandbox/primary_output.bin ] && exit_code == 0

[SECTION: ASSEMBLE_FINAL_BUILD]
DEPENDS : [PROCESS_PRIMARY_STREAM]
INPUTS  : [".tmp/sandbox/primary_output.bin"]
OP      : <ASSEMBLY_OPCODE_WITH_FLAGS>
OUT     : ".tmp/build/final_artifact.bin"
ASSERT  : [ -f .tmp/build/final_artifact.bin ] && exit_code == 0 && zero_clipping == true
