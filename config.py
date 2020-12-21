class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "92796c15-2f29-4d0a-8c9c-14f90d03bb27"  

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    #AUTHORITY = "https://login.microsoftonline.com/eec8b34d-bb0c-45d8-bee6-34c5a32199f8"

    # TODO: Enter your application client ID here
    CLIENT_ID = "7fd8f8fb-cff9-49d1-b3bd-1243e8d89792"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session