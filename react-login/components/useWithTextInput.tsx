import { useState } from 'react';

type Event = { target: { value: string }};

export type InputType = 'text' | 'password';

export type TextInputBinding = {
    type: InputType;
    value: string;
    onChange: (event: Event) => void;
};

export const useWithTextInput = (type: InputType = 'text'): TextInputBinding => {
    const [inputValue, setInputValue] = useState<string>('');
    const onChange = (e: Event) => {
        setInputValue(e.target.value);
    };

    return {
        type,
        value: inputValue,
        onChange,
    };
};
