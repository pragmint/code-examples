import React from 'react';
import styled, { css, DefaultTheme, StyledComponent } from 'styled-components';

export enum IconSide {
    RIGHT,
    LEFT,
}

const buttonBase = css`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    height: 5rem;
    border: none;
    border-radius: 1rem;
    padding-left: 2.2rem;
    padding-right: 2.2rem;
    font-size: 1.6rem;
`;

export enum ButtonType {
    DEFAULT,
    INVERSE,
    GHOST,
    RED_GHOST,
}

const DefaultButton = styled.button`
    ${buttonBase}
    background-color: #1FA889;
    font-weight: bolder;
    color: white;
`;

const InverseButton = styled.button``;

const Ghost = styled.button``;

const RedGhost = styled.button``;

type OnClick = (event?: React.MouseEvent<HTMLButtonElement>) => void;


const getStyledButton = (type: ButtonType) => {
    switch (type) {
        case ButtonType.INVERSE: return InverseButton;
        case ButtonType.RED_GHOST: return RedGhost;
        case ButtonType.GHOST: return Ghost;
        default: return DefaultButton;
    }
};

type ButtonProps = {
    id: string | undefined;
    text: string;
    icon: React.ReactElement | null;
    iconIsOnLeft: boolean;
    iconIsOnRight: boolean;
    ButtonComponent: StyledComponent<'button', DefaultTheme, Record<string, unknown>, never>;
    autoFocus: boolean;
    onClick: OnClick;
};

const Button = ({
    id,
    text,
    icon,
    iconIsOnLeft,
    iconIsOnRight,
    ButtonComponent,
    autoFocus = false,
    onClick,
}: ButtonProps) => {
    return (
        <ButtonComponent id={id} onClick={onClick} autoFocus={autoFocus}>
            {iconIsOnLeft && <>{ icon}<span style={{ paddingLeft: '1rem' }}>{text}</span></>}
            {iconIsOnRight && <><span style={{ paddingRight: '1rem' }}>{text}</span>{icon}</>}
            {icon === null && text}
        </ButtonComponent>
    );
};

type UseWithButtonArgs = {
    id: string;
    text: string;
    icon?: React.ReactElement | null;
    iconSide?: IconSide;
    type?: ButtonType;
    autoFocus?: boolean;
    onClick: OnClick;
};

export const useWithButton = ({
    id,
    text,
    icon = null,
    iconSide = IconSide.LEFT,
    type = ButtonType.DEFAULT,
    autoFocus = false,
    onClick,
}: UseWithButtonArgs): ButtonProps => {
    const ButtonComponent = getStyledButton(type);
    const iconIsOnLeft = (icon !== null && iconSide === IconSide.LEFT);
    const iconIsOnRight = (icon !== null && iconSide === IconSide.RIGHT);
    return {
        id,
        text,
        icon,
        iconIsOnLeft,
        iconIsOnRight,
        ButtonComponent,
        autoFocus,
        onClick,
    };
};

export default Button;