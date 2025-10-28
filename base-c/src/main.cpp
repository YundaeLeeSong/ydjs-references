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

     rm -rf build
     cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=../ext/vcpkg/scripts/buildsystems/vcpkg.cmake

     cmake --build build                        (single-config)
     cmake --build build --config Release       (multi-config, e.g., Visual Studio)

     ./build/my_app             (Linux / macOS)
     ./build/Release/my_app.exe (Windows, Visual Studio)
*/





// --- Dependency 1: {fmt} ---
#include <fmt/core.h>

// --- Dependency 2: Qt 5 ---
#include <QApplication>
#include <QLabel>
#include <QString>
#include <QWidget>
#include <QVBoxLayout>

// Other includes
#include <string>

int main(int argc, char *argv[]) {
    // 1. Create the Qt Application
    QApplication app(argc, argv);

    // 2. Create our main window
    QWidget window;
    window.setWindowTitle("App using fmt + Qt");
    window.resize(300, 100);

    // 3. --- USE BOTH LIBRARIES ---
    //    Use fmt::format() to create a standard string
    std::string app_name = "vcpkg";
    std::string text = fmt::format("Hello from {fmt} and Qt 6 in the same app (powered by {})!", app_name);

    //    Convert the std::string to a QString for Qt
    QString q_text = QString::fromStdString(text);
    // 4. ------------------------


    // 5. Create a Qt label with our formatted string
    QLabel *label = new QLabel(q_text);

    // 6. Set up the layout and show the window
    QVBoxLayout *layout = new QVBoxLayout();
    layout->addWidget(label);
    window.setLayout(layout);
    window.show();

    // 7. Start the Qt event loop
    return app.exec();
}