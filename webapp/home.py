import justpy as jp
from webapp.layout import DefaultLayout
from webapp.page import Page

class Home(Page):
    path= "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind= True)

        lay = DefaultLayout(a=wp, view = "hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container,  classes = "bg-gray-200 h-screen")
        jp.Div(a = div, text= "Home page", 
                classes = "text-4xl m-2" )
        jp.Div( a = div, text ="""
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
        It has survived not only five centuries, but also the leap into electronic typesetting, 
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
        sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
        PageMaker including versions of Lorem Ipsum.
        
        """, classes= "text-lg p-2")
        return wp

    