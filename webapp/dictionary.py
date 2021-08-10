import justpy as jp
import sys
sys.path.append('E:\Python projects\Instant-dictionary-webapp')
from definition import Definition


class Dictionary:
    path= "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind= True)
        div = jp.Div(a=wp,  classes = "bg-gray-200 h-screen")
        jp.Div(a=div, text= "instant dictionary", classes= "text-4xl m-2")
        jp.Div(a= div, text="get definition of any english word", classes="text-lg")

        user_input = jp.Input(a=div, placeholder = "type a word",
                classes = "m-2 bg-gray-100 border-2 border-gray-200 rounded "
                        "w-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4")
        output = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        jp.Button(a=div, text="find", click = cls.find, user_input = user_input, output = output, 
        classes= "border border-blue-500 m-2 py-1 px-4"
         " rounded text-blue-600 hover:bg-red-500"
         " hover:text-white")
        return wp

    @staticmethod
    def find(widget, msg):
        term = widget.user_input.value
        definition_obj = Definition(term)
        widget.output.text = definition_obj.get()
        # widget.output.text = term
       
    

