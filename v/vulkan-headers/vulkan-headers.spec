Name: vulkan-headers
Version: 1.3.277
Release: alt1
Summary: Khronos group Vulkan API SDK headers

Group: Development/C++
License: Apache-2.0
Url: https://github.com/KhronosGroup/Vulkan-Headers

Source: %name-%version.tar

BuildRequires(pre): cmake rpm-build-python3
BuildRequires: gcc-c++

BuildArch: noarch

%description
Development headers for Vulkan applications.

%package -n vulkan-registry
Summary: Vulkan API registry
Group: Development/C++
BuildArch: noarch
Requires: vulkan-filesystem

# filter out self-provided requires
%add_python3_req_skip spec_tools.util

%description -n vulkan-registry
Vulkan SDK API registry files.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_includedir/vulkan
%_includedir/vk_video
%dir %_datadir/cmake/VulkanHeaders
%_datadir/cmake/VulkanHeaders/*.cmake

%files -n vulkan-registry
%_datadir/vulkan/registry

%changelog
* Thu Mar 07 2024 L.A. Kostis <lakostis@altlinux.ru> 1.3.277-alt1
- Split out headers and registry to ease build.
