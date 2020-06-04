import React from "react";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faWindowClose} from "@fortawesome/free-solid-svg-icons";

const CloseButton = ({classSize, className, onClick, colorButton}) => {
    return (
        <p className={`pointer ${classSize}`}>
            <FontAwesomeIcon icon={faWindowClose} className={className} onClick={onClick} color={colorButton}/>
        </p>
    )
}

export default CloseButton;