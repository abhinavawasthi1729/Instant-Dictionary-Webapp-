import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind= True)
        div = jp.Div(a=wp,  classes = "bg-gray-200 h-screen")
        jp.Div(a = div, text= "About page", 
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

jp.Route(About.path, About.serve)
jp.justpy()