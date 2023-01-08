import { SetStateAction, Dispatch, FormEvent, useState } from "react";
import { TableContents } from "../Table/Table";

interface AlertModalProps {
    useContents: Dispatch<SetStateAction<TableContents>>,
}

export default function AlertModal({ useContents }: AlertModalProps) {

    function onSubmitEvent(e: FormEvent<HTMLFormElement>) {
        e.preventDefault();
        // hint: the alert given is at (e.target as any).elements[0].value - ignore typescript being annoying
        console.log((e.target as any)[0].value);

        console.log(useState);
        console.log(useContents);
    }

    return (
        <form data-testid='form' onSubmit={onSubmitEvent}>
            <label> Add new alert: </label>
            <input type='text' id='alert' name='alert' />
            <button type='submit'> Add </button>
        </form>
    )
}
