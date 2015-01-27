import cx_Freeze

executables = [cx_Freeze.Executable("example.py")]


cx_Freeze.setup(
    name="ezTextExample",
    options={"build_exe":{"packages":["pygame","time","random",
                                      "math","numpy","sys","string",
                                      "pygame.locals"],
                          "include_files":["eztext.py","Times_New_Roman.ttf"]}},
    description = "simple software",
    executables = executables    
)
