// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';

import BarChart from '@cloudscape-design/components/bar-chart';
import Header from '@cloudscape-design/components/header';
import Link from '@cloudscape-design/components/link';
import Editor from '@monaco-editor/react';

import { WidgetConfig } from '../interfaces';

function EditorHeader() {
  return (
    <Header variant="h2" description="The VisQL Editor.">
        VisQL Editor
    </Header>
  );
}

function EditorContent({ onEditorChange} ) {
  function handleEditorChange(value, event) {
    onEditorChange(value);
  }

  return (
    <Editor height="90vh" defaultLanguage="python" onChange={handleEditorChange}/>
  );
}
export const editor: WidgetConfig = {
  definition: { defaultRowSpan: 4, defaultColumnSpan: 2, minRowSpan: 3 },
  data: {
    title: 'Editor',
    description: 'VisQL Editor',
    header: EditorHeader,
    content: EditorContent,
    staticMinHeight: 560,
  },
};