var xmlns="http://www.w3.org/2000/svg"
function zoomNode(node){
    if (!node.hasAttribute("zoomed")){
        node.setAttribute("zoomed","0")
    }
    text_elements=node.getElementsByTagName("text")
    if (node.getAttribute("zoomed") == "0"){
        node.parentNode.appendChild(node);
        x=text_elements[0].getAttribute("x")
        y=text_elements[0].getAttribute("y")
        node.setAttribute("transform","translate(" + -x + "," + -y + ") scale(2)");
        node.setAttribute("zoomed","1");

        for (i=0; i<3;i++){
            text_elements[i].setAttribute("font-size","14.00")
            text_elements[i].removeAttribute("transform")
        }
        for (i=3; i<text_elements.length;i++){
            text_elements[i].setAttribute("visibility","visible")
        }
    } else {
        node.setAttribute("transform","scale(1)");
        node.setAttribute("zoomed","0");

        for (i=0; i<3;i++){
            var transform_x = i*10;
            text_elements[i].setAttribute("font-size","18.00")
            text_elements[i].setAttribute("transform","translate(0 "+transform_x+")")
        }
        for (i=3; i<text_elements.length;i++){
            text_elements[i].setAttribute("visibility","hidden")
        }
    }
}
