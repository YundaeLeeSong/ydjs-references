# src/app/CMakeLists.txt

add_executable(my_app
    main.cpp
)

# Link our app against the libraries
# CMake automatically handles finding libcore and libcount
# from the other directories.
target_link_libraries(my_app
  PRIVATE
    libcore
    libcount
)


