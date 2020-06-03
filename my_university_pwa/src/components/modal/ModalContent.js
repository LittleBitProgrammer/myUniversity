import React from "react";

const ModalContent = ({children, className}) => {
    return (
        <div className={className}>
            {children}
        </div>
    )
}

export default ModalContent;