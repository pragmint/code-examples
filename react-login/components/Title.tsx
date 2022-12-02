import React, { ReactNode } from 'react';
import styled from 'styled-components';

const Container = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
`;

const Text = styled.span`
    font-size: 2.8rem;
    font-weight: bold;
`;

const Spacer = styled.div`
    width: .8rem;
`;

const Line = styled.div`
    width: 4rem;
    height: .3rem;
    background-color: black;
`;

const Title: React.FC<Record<string, ReactNode>> = ({ children }) => {
    return (
        <Container>
            <Text>{children}</Text>
            <Spacer />
            <Line />
        </Container>
    );
};

export default Title;