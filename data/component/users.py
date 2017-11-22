"""
Component: Users
"""
# component json
user_json = {
    "User_component" : {
        "id" : "Users",
        "icon" : "fa-home",
        "status" : True,
        "order" : 1,
        "tab_group_name" : "user_tab_group",
        "tab" : [
            {
                "tab_name" : "General",
                "tab_id" : "general",
                "tab_icon" : "fa-user",
                "tab_type" : "basic",
                "tab_content" : []
            },
            {
                "tab_name" : "Accounts",
                "tab_id" : "accounts",
                "tab_icon" : "fa-key",
                "tab_type" : "list",
                "tab_content" : [
                    {
                        "tab_item_name": "1 First"
                    },
                    {
                        "tab_item_name": "2 Second"
                    },
                    {
                        "tab_item_name": "3 Second"
                    }
                ]
            },
            {
                "tab_name" : "Help",
                "tab_id" : "help",
                "tab_icon" : "fa-question",
                "tab_type" : "basic",
                "tab_content" : []
            }
        ]
    }
}

class Component:
    def __init__(self):
        pass

    def execute(self):
        pass

    def build_ui(self):

        pass
