import React from "react";
import Row from "../bootstrap/Row";
import Column from "../bootstrap/Column";
import CloseButton from "../icons/CloseButton";
import JumbotronFluid from "../bootstrap/JumbotronFluid";




const ModalHeader = ({className, title, onCloseClick, textSize, color, iconSize}) => {
    return (
        <div className={className}>
            <JumbotronFluid>
                <Row className="justify-content-between p-2">
                    <Column columnSize="10">
                        <p className={`${textSize} text-${color}`}>{title}</p>
                    </Column>
                    <Column columnSize="2">
                        <CloseButton className="float-right" classSize={iconSize} onClick={onCloseClick} colorButton="white"/>
                    </Column>
                </Row>
            </JumbotronFluid>
        </div>
    )
}

export default ModalHeader;