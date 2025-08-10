// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';

import Grid from '@cloudscape-design/components/grid';

import {
  BaseStaticWidget,
  editor,
  diagram,
} from '../widgets';

export function Content({onEditorChange, jsonSpec}: {onEditorChange: (value: string) => void , jsonSpec: Record<string, any>}) {
  return (
    <Grid
      gridDefinition={[
        { colspan: { l: 6, m: 6, default: 12 } },
        { colspan: { l: 6, m: 6, default: 12 } },
      ]}
    >
      <BaseStaticWidget key={0} config={editor.data} onEditorChange={onEditorChange}/>
      <BaseStaticWidget key={1} config={diagram.data} jsonSpec={jsonSpec}/>
    </Grid>
  );
}