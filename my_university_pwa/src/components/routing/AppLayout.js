import React from 'react';

const AppLayout = (props) => {
    return (
        <div>
                {props.navBar ? React.createElement(props.navBar) : null}
                {props.children}
        </div>
    );
};

export default AppLayout;