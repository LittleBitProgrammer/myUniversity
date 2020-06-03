import React from "react";
import ModalContent from "./ModalContent";

const Modal = ({children, className, classContent}) => {
    return (
        <div className={className}>
            <ModalContent className={classContent}>
                {children}
            </ModalContent>
        </div>
    )
}

export default Modal;