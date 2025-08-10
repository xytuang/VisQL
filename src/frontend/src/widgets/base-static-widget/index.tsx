// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import React from 'react';

import Container from '@cloudscape-design/components/container';

import { WidgetDataType } from '../interfaces';

import * as styles from './styles.module.scss';

export function BaseStaticWidget({ config, onEditorChange, jsonSpec }: { config: WidgetDataType, onEditorChange?: (value: string) => void, jsonSpec: Record<string, any> }) {
  const Wrapper = config.provider ?? React.Fragment;
  return (
    <div className={styles.staticWidget} style={{ minHeight: config.staticMinHeight }}>
      <Wrapper>
        <Container
          header={<config.header />}
          fitHeight={true}
          footer={config.footer && <config.footer />}
          disableContentPaddings={config.disableContentPaddings}
        >
          <config.content onEditorChange={onEditorChange} jsonSpec={jsonSpec}/>
        </Container>
      </Wrapper>
    </div>
  );
}