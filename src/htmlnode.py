class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ''
        for attribute in self.props:
            html_string += ' ' + attribute + '=' + f'"{self.props[attribute]}"'
        return html_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError('value is None')
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('tag is None')
        if self.children == None:
            raise ValueError('children is None')
        html_string = ''
        for child_node in self.children:
            html_string += child_node.to_html()
        return f'<{self.tag}>' + html_string + f'</{self.tag}>'
    

if __name__=="__main__":
    # node = HTMLNode()
    # print('Empty object of HTMLNode', node)

    # node2 = HTMLNode('h1', 'Header', props={"href": "https://www.google.com", "target": "_blank",})
    # print(node2.props_to_html())

    # leaf_node = LeafNode('a', 'something text', {"href": "https://www.google.com"})
    # print(leaf_node.to_html())

    # leaf_node2 = LeafNode("p", "This is a paragraph of text.")
    # print(leaf_node2.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())