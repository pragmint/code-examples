import React from 'react';
import { useUserContext } from './UserContext';
import { login } from './login';
import Button, { useWithButton } from './Button';
import LabeledInput, { useWithLabeledInput } from './LabeledInput';
import Title from './Title';
import styled from 'styled-components';

const Container = styled.div`
    width: 40rem;
`;

const Form = styled.div`
    display: flex;
    flex-direction: column;
    max-width: 40rem;
`;

const SmallVerticalSpacer = styled.div`
    height: 2rem;
`;

const LargeVerticalSpacer = styled.div`
    height: 3rem;
`;

const LoginForm = () => {
    const {
        email,
        password,
        loginButton,
    } = useLoginForm();

    return (
        <Container>
            <Title>Login</Title>
            <Form>
                <LargeVerticalSpacer />
                <LabeledInput { ...email} />
                <SmallVerticalSpacer />
                <LabeledInput { ...password} />
                <LargeVerticalSpacer />
                <Button { ...loginButton} />
                <LargeVerticalSpacer />
            </Form>
        </Container>
    );
};


const useLoginForm = () => {
    const user = useUserContext();

    const email = useWithLabeledInput({
        id: 'email-input',
        text: 'Username',
    });
    
    const password = useWithLabeledInput({
        id: 'password-input',
        text: 'Password',
        type: 'password',
    });

    const onSubmit = async () => {
        const loginResponse = await login(email.value, password.value);
        if (!loginResponse.hasError) {
            user.setUser(loginResponse.userData);
            // you could also add a cookie here.
        }
    };

    const loginButton = useWithButton({
        id: 'login-button',
        text: 'Login',
        onClick: onSubmit,
    });

    // I also have usually would an effect here for loading cookies into state
    // on first render

    return {
        email,
        password,
        loginButton,
    };
};

export default LoginForm;