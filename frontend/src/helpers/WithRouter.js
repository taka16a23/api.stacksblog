import { useParams, useNavigate } from "react-router-dom";

export default function withRouter( Child ) {
  return ( props ) => {
    const params = useParams();
    const navigate = useNavigate();
    return <Child { ...props } params ={ params } />;
  }
}
