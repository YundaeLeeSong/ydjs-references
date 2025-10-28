// src/main.cpp

/*
 Build / run instructions (clean, concise)

 Prerequisites
    - CMake installed and on PATH
    - vcpkg cloned and bootstrapped (example location used below: ../ext/vcpkg)
        Example:
            git clone https://github.com/microsoft/vcpkg.git ../ext/vcpkg
            # Linux/macOS
            ../ext/vcpkg/bootstrap-vcpkg.sh
            # Windows (PowerShell / cmd)
            ../ext/vcpkg/bootstrap-vcpkg.bat

 Why the toolchain file?
    - Even in vcpkg "manifest mode" (presence of vcpkg.json), CMake still needs
        the vcpkg toolchain file so it knows to use vcpkg-managed packages:
            -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake

 Typical workflow (manifest mode)
    1) Configure (create build directory and tell CMake to use vcpkg):
         cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake
         # For single-config generators you can also set build type:
         # cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=... -DCMAKE_BUILD_TYPE=Release

    2) Build:
         # Multi-config generators (Visual Studio) - specify --config:
         cmake --build build --config Release
         # Single-config (Ninja, Makefiles):
         cmake --build build

    3) Run the executable
         # Linux / macOS (executable name shown as my_app)
         ./build/my_app
         # Windows (multi-config Visual Studio)
         .\build\Release\my_app.exe
         # Windows (single-config generator)
         .\build\my_app.exe

 Notes
    - When CMake configures the project it will detect vcpkg.json (manifest mode),
        vcpkg will download & install declared dependencies (e.g., "fmt") and
        CMake will be able to find and link them automatically.
    - If your vcpkg root is in a different location, update the -DCMAKE_TOOLCHAIN_FILE path.
    - To see detailed build output:
            cmake --build build --config Release --verbose
    - To clean and reconfigure, remove the build directory:
            rm -rf build   # or use Explorer / rmdir on Windows

 Example (all together)
     rm -rf build               (Linux / macOS)
     rmdir /s /q build          (Windows, cmd)

     cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake
     


     cmake --build build                        (single-config)
     cmake --build build --config Release       (multi-config, e.g., Visual Studio)

     cmake --build build --config Release
     cmake --install build --config Release

     export PATH="build/vcpkg_installed/x64-windows/bin:$PATH"
     ./build/Release/my_app.exe

     ./build/my_app             (Linux / macOS)
     ./build/Release/my_app.exe (Windows, Visual Studio)
*/



/*
    < Shortcut > Build / run instructions (concise)
     rm -rf build
     cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake
     cmake --build build --config Release
     ./build/Release/qt_vcpkg_demo.exe
*/

#include <QApplication>
#include <QPushButton>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>
#include <QString>
#include <fmt/format.h>

int main(int argc, char **argv) {
    QApplication app(argc, argv);

    QWidget window;
    window.setWindowTitle("Qt + vcpkg Demo");

    auto *label = new QLabel("Press the button");
    auto *button = new QPushButton("Click me");

    // simple counter using lambda slot
    QObject::connect(button, &QPushButton::clicked, [&]() {
        static int count = 0;
        ++count;
        std::string s = fmt::format("Clicked {} time{}", count, (count == 1 ? "" : "s"));
        label->setText(QString::fromStdString(s));
    });

    auto *layout = new QVBoxLayout;
    layout->addWidget(label);
    layout->addWidget(button);
    window.setLayout(layout);

    window.show();
    return app.exec();
}
