from conans import ConanFile, CMake


class gdal_translate(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = [
        "gdal/3.5.2@terranum-conan+gdal/stable",
        ]

    generators = "cmake", "gcc", "txt"

    # this isn't needed anymore with wxWidgets 3.2.0 (using GTK 3.0)
    def configure(self):
            self.options["gdal"].with_curl = True # for xml support
            self.options["gdal"].shared = True
    #    if self.settings.os == "Linux":
    #        self.options["wxwidgets"].webview = False # webview control isn't available on linux.

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")  # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib")  # From lib to bin

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
