#!/usr/bin/python3
import subprocess
import shutil

# run from the odin_vma source directory
prefix = 'VulkanMemoryAllocator'
source_files = [
    # f'{prefix}/src/VmaUsage.h',
    f'{prefix}/src/VmaUsage.cpp',
]

# define, desc, value
defines = [
    ("VMA_STATIC_VULKAN_FUNCTIONS"                      , "Link statically with Vulkan API"                                                   , False),
    ("VMA_DYNAMIC_VULKAN_FUNCTIONS"                     , "Fetch pointers to Vulkan functions internally (no static linking)"                 , False),
    ("VMA_DEBUG_ALWAYS_DEDICATED_MEMORY"                , "Every allocation will have its own memory block"                                   , False),
    ("VMA_DEBUG_INITIALIZE_ALLOCATIONS"                 , "Automatically fill new allocations and destroyed allocations with some bit pattern", False),
    ("VMA_DEBUG_GLOBAL_MUTEX"                           , "Enable single mutex protecting all entry calls to the library"                     , False),
    ("VMA_DEBUG_DONT_EXCEED_MAX_MEMORY_ALLOCATION_COUNT", "Never exceed VkPhysicalDeviceLimits::maxMemoryAllocationCount and return error"    , False),
    ("VMA_STATS_STRING_ENABLED"                         , "snprintf moment", False),
]


compiler = 'clang'
cmd = [ compiler, '-c', f'-I{prefix}/include/', '-o', 'libVMA.o']
cmd += source_files
print(cmd)

for d in defines:
    print(d[0], d[1], d[2], '\n')
    cmd += [f'-D{d[0]}={1 if d[2] else 0}']
result = subprocess.run(' '.join(cmd), check=True, shell=True)

if result.returncode == 0: 
    shutil.move("./libVMA.o", "./external/")
