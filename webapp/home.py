import justpy as jp


class Home:
    path= "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind= True)
        div = jp.Div(a=wp,  classes = "bg-gray-200 h-screen")
        jp.Div(a = div, text= "Home page", 
                classes = "text-4xl m-2" )
        jp.Div( a = div, text ="""
        ok 
        test 
        sahi 
        lorem
        is 
        not 
        working 
        
        """, classes= "text-lg")
        return wp
