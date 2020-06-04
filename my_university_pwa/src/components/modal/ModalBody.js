import React from "react";

const ModalBody = ({children, className}) => {
    return (
        <div className={className}>
            {children}
        </div>
    )
}

export default ModalBody;