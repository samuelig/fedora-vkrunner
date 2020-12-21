%global gitrev 1b4cc6b129e857d88ba9487bc8a4983d6a11df02
%global shortgit 1b4cc6b

Name:           vkrunner
Version:        0.1.20201230
Release:        1.git%{shortgit}%{?dist}
Summary:        A shader script tester for Vulkan

License:        MIT
URL:            https://github.com/Igalia/vkrunner/
Source0:        %{URL}/archive/%{gitrev}/%{name}-%{gitrev}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  vulkan-headers
Requires:       glslang
Requires:       spirv-tools
Requires:       vulkan-loader

%description
VkRunner is a Vulkan shader tester based on shader_runner in Piglit.

The goal is to make it be able to test scripts as similar to Piglit's
shader_test format as possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
VkRunner is a Vulkan shader tester based on shader_runner in Piglit.

The goal is to make it be able to test scripts as similar to Piglit's
shader_test format as possible.

%prep
%autosetup -n %{name}-%{gitrev}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md examples
%{_bindir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libvkrunner.a
%{_libdir}/pkgconfig/vkrunner.pc

%changelog
* Wed Dec 30 2020 Samuel Iglesias Gonsálvez <siglesias@igalia.com> - 0.1.20201230-1.git1b4cc6b
- First package.


# vi:sw=4 ts=8 et
