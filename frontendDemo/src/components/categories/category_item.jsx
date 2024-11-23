import { ListGroup } from "react-bootstrap"


const CategoryItem = ({id,name})=>{
    return(
        <ListGroup>
            <ListGroup.Item>
                <h1>ID {id}</h1>
                <p>name {name}</p>
            </ListGroup.Item>
        </ListGroup>
    )
}
export default CategoryItem;