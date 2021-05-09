
































import sys, os
sys.path.append("."."/"."."")""
""#"" ""f""a""c""e""r""e""c""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""f""e""a""t""u""r""e"" ""i""m""p""o""r""t"" ""F""i""s""h""e""r""f""a""c""e""s"","" ""P""C""A"","" ""S""p""a""t""i""a""l""H""i""s""t""o""g""r""a""m"","" ""I""d""e""n""t""i""t""y""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""d""i""s""t""a""n""c""e"" ""i""m""p""o""r""t"" ""E""u""c""l""i""d""e""a""n""D""i""s""t""a""n""c""e"","" ""C""h""i""S""q""u""a""r""e""D""i""s""t""a""n""c""e""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""c""l""a""s""s""i""f""i""e""r"" ""i""m""p""o""r""t"" ""N""e""a""r""e""s""t""N""e""i""g""h""b""o""r""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""m""o""d""e""l"" ""i""m""p""o""r""t"" ""P""r""e""d""i""c""t""a""b""l""e""M""o""d""e""l""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""v""a""l""i""d""a""t""i""o""n"" ""i""m""p""o""r""t"" ""K""F""o""l""d""C""r""o""s""s""V""a""l""i""d""a""t""i""o""n""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""v""i""s""u""a""l"" ""i""m""p""o""r""t"" ""s""u""b""p""l""o""t""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""u""t""i""l"" ""i""m""p""o""r""t"" ""m""i""n""m""a""x""_""n""o""r""m""a""l""i""z""e""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""s""e""r""i""a""l""i""z""a""t""i""o""n"" ""i""m""p""o""r""t"" ""s""a""v""e""_""m""o""d""e""l"","" ""l""o""a""d""_""m""o""d""e""l""
""#"" ""r""e""q""u""i""r""e""d"" ""l""i""b""r""a""r""i""e""s""
""i""m""p""o""r""t"" ""n""u""m""p""y"" ""a""s"" ""n""p""
""#"" ""t""r""y"" ""t""o"" ""i""m""p""o""r""t"" ""t""h""e"" ""P""I""L"" ""I""m""a""g""e"" ""m""o""d""u""l""e""
""t""r""y"":""
"" "" "" "" ""f""r""o""m"" ""P""I""L"" ""i""m""p""o""r""t"" ""I""m""a""g""e""
""e""x""c""e""p""t"" ""I""m""p""o""r""t""E""r""r""o""r"":""
"" "" "" "" ""i""m""p""o""r""t"" ""I""m""a""g""e""
""i""m""p""o""r""t"" ""m""a""t""p""l""o""t""l""i""b"".""c""m"" ""a""s"" ""c""m""
""i""m""p""o""r""t"" ""l""o""g""g""i""n""g""
""i""m""p""o""r""t"" ""m""a""t""p""l""o""t""l""i""b"".""p""y""p""l""o""t"" ""a""s"" ""p""l""t""
""i""m""p""o""r""t"" ""m""a""t""p""l""o""t""l""i""b"".""c""m"" ""a""s"" ""c""m""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""l""b""p"" ""i""m""p""o""r""t"" ""L""P""Q"","" ""E""x""t""e""n""d""e""d""L""B""P""
""
""c""l""a""s""s"" ""F""i""l""e""N""a""m""e""F""i""l""t""e""r"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""n""a""m""e"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""n""a""m""e"" ""="" ""n""a""m""e""
""
"" "" "" "" ""d""e""f"" ""_""_""c""a""l""l""_""_""(""s""e""l""f"","" ""f""i""l""e""n""a""m""e"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
"" "" "" "" "" "" "" "" ""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
    