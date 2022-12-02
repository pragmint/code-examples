import React from 'react';
import styled from 'styled-components';
import { InputType, TextInputBinding, useWithTextInput } from './useWithTextInput';

const Label = styled.label`
    color: #2D2D2D;
    display: block;
`;

const Input = styled.input`
    display: block;
    background-color: #F5F5F5;
    
    width: 100%;
    height: 5.4rem;
    
    box-sizing: border-box;
    
    padding: 1.8rem;

    border-color: #DDE5E9;
    border-width: 1px;
    border-radius: 1rem;
    border-style: solid;
   
    margin-top: 1rem;

    font-size: 1.6rem;
    outline: none;
    
    :focus {
        border-color: #1FA889;
        border-width: .2rem;
        padding: 1.7rem;
        padding-left: 1.8rem;
    }
`;

type LabeledInputProps = {
    id: string;
    text: string;
    set: (text: string) => void;
    placeholder: string;
    binding: TextInputBinding;
    value: string;
};

const LabeledInput = ({ id, text, placeholder, binding }: LabeledInputProps) => {
    return (
        <div>
            <Label htmlFor={id}>{text}</Label>
            <Input
                id={id}
                name={id}
                placeholder={placeholder}
                {...binding}
            />
        </div>
    );
};

type UseWithLabeledInputArgs = {
    id: string;
    text: string;
    type?: InputType;
};

export const useWithLabeledInput = ({
    id,
    text,
    type = 'text',
}: UseWithLabeledInputArgs): LabeledInputProps => {
    const binding = useWithTextInput(type);
    return {
        id,
        text,
        placeholder: text,
        set: (text: string) => binding.onChange({ target: { value: text }}),
        value: binding.value,
        binding,
    };
};

export default LabeledInput;