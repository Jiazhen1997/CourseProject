
































import cStringIO
import base64

try:
    from PIL import Image
except ImportError:
    import Image


from flask import Flask, request, request_finished, json, abort, make_response, Response, jsonify


import sys
sys.path.append("."."/"."."/"."."")""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""m""o""d""e""l"" ""i""m""p""o""r""t"" ""P""r""e""d""i""c""t""a""b""l""e""M""o""d""e""l""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""l""b""p"" ""i""m""p""o""r""t"" ""E""x""t""e""n""d""e""d""L""B""P""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""f""e""a""t""u""r""e"" ""i""m""p""o""r""t"" ""S""p""a""t""i""a""l""H""i""s""t""o""g""r""a""m""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""d""i""s""t""a""n""c""e"" ""i""m""p""o""r""t"" ""C""h""i""S""q""u""a""r""e""D""i""s""t""a""n""c""e""
""f""r""o""m"" ""f""a""c""e""r""e""c"".""c""l""a""s""s""i""f""i""e""r"" ""i""m""p""o""r""t"" ""N""e""a""r""e""s""t""N""e""i""g""h""b""o""r""
""
""#"" ""l""o""g""g""i""n""g""
""i""m""p""o""r""t"" ""l""o""g""g""i""n""g""
""f""r""o""m"" ""l""o""g""g""i""n""g"".""h""a""n""d""l""e""r""s"" ""i""m""p""o""r""t"" ""R""o""t""a""t""i""n""g""F""i""l""e""H""a""n""d""l""e""r""
""
""#"" ""t""h""e"" ""w""e""b""s""e""r""v""e""r"" ""r""e""c""o""g""n""i""t""i""o""n"" ""m""o""d""u""l""e""
""i""m""p""o""r""t"" ""r""e""c""o""g""n""i""t""i""o""n""
""
""#"" ""T""h""e"" ""m""a""i""n"" ""a""p""p""l""i""c""a""t""i""o""n"":"" ""
""a""p""p"" ""="" ""F""l""a""s""k""(""_""_""n""a""m""e""_""_"")""
""
""#"" ""T""h""i""s"" ""i""s"" ""a"" ""l""i""s""t"" ""o""f"" ""e""r""r""o""r""s"" ""t""h""e"" ""W""e""b""s""e""r""v""i""c""e"" ""r""e""t""u""r""n""s""."" ""Y""o""u"" ""c""a""n"" ""c""o""m""e"" ""u""p""
""#"" ""w""i""t""h"" ""n""e""w"" ""e""r""r""o""r"" ""c""o""d""e""s"" ""a""n""d"" ""p""l""u""g"" ""t""h""e""m"" ""i""n""t""o"" ""t""h""e"" ""A""P""I"".""
""#""
""#"" ""A""n"" ""e""x""a""m""p""l""e"" ""J""S""O""N"" ""r""e""s""p""o""n""s""e"" ""f""o""r"" ""a""n"" ""e""r""r""o""r"" ""l""o""o""k""s"" ""l""i""k""e"" ""t""h""i""s"":""
""#""
""#"" "" "" ""{""  Decodes Base64 image data, reads it with PIL and converts it into grayscale.

    Args:
    
        base64_image [string] A Base64 encoded image (all types PIL supports).
    