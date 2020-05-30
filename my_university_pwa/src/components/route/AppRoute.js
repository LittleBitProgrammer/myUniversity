import React from 'react';
import { Route } from 'react-router-dom';
import AppLayout from './AppLayout';

const AppRoute = ({ component, ...routeProps }) => {
    return (
        <Route {...routeProps} render={(props) => {
            return (
                <AppLayout { ...props} {...routeProps}>
                    {React.createElement(component, props)}
                </AppLayout>
            );
        }} />
    );
};

export default AppRoute;