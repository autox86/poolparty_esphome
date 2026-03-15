## 🏅 Pool pH Tank-Steuerung

Hier ist die Konfiguration für die **Mushroom Template Badge**, um den Füllstand des pH-Tanks im Dashboard anzuzeigen:

```yaml
type: custom:mushroom-template-badge
entity: binary_sensor.pool_ph_tank_leer
content: |-
  {% if is_state('binary_sensor.pool_ph_tank_leer', 'on') %}
    Tankinhalt: LEER!
  {% else %}
    Tankinhalt: {{ states('sensor.pool_ph_tank_restinhalt') }}L
  {% endif %}
icon: |-
  {{ 'mdi:alert-circle' if is_state('binary_sensor.pool_ph_tank_leer', 'on')
  else 'mdi:ph' }}
color: |-
  {{ 'red' if is_state('binary_sensor.pool_ph_tank_leer', 'on') 
  else 'dodgerblue' }}
tap_action:
  action: call-service
  service: button.press
  target:
    entity_id: button.pool_ph_tank_reset

```

---

```yaml
type: custom:mushroom-template-badge
entity: binary_sensor.pool_low_salt_meldung
content: Salz niedrig!
icon: mdi:shaker
color: orange
visibility:
  - condition: state
    entity: binary_sensor.pool_low_salt_meldung
    state: "on"
tap_action:
  action: none
hold_action:
  action: none

```

---

```yaml
type: custom:mushroom-template-badge
entity: binary_sensor.pool_tuya_hardware_defekt
content: |-
  {% if is_state('binary_sensor.pool_tuya_hardware_defekt', 'on') %}
    Tuya: FEHLER!
  {% else %}
    Tuya: OK
  {% endif %}
icon: >-
  {{ 'mdi:alert-octagon' if is_state('binary_sensor.pool_tuya_hardware_defekt',
  'on')

  else 'mdi:chip' }}
color: |-
  {{ 'crimson' if is_state('binary_sensor.pool_tuya_hardware_defekt', 'on') 
  else 'limegreen' }}
tap_action:
  action: call-service
  service: button.press
  target:
    entity_id: button.pool_tuya_fehler_reset


```

---

```yaml
type: custom:mushroom-template-badge
entity: binary_sensor.pool_chlorinator_hardware_defekt
content: |-
  {% if is_state('binary_sensor.pool_chlorinator_hardware_defekt', 'on') %}
    Chlorinator: DEFEKT
  {% else %}
    Chlorinator: OK
  {% endif %}
icon: >-
  {{ 'mdi:alert-octagon' if
  is_state('binary_sensor.pool_chlorinator_hardware_defekt', 'on')

  else 'mdi:chip' }}
color: >-
  {{ 'crimson' if is_state('binary_sensor.pool_chlorinator_hardware_defekt',
  'on') 

  else 'limegreen' }}
tap_action:
  action: call-service
  service: button.press
  target:
    entity_id: button.pool_chlorinator_fehler_reset


```

---

```yaml
type: custom:mushroom-template-badge
entity: binary_sensor.pool_pumpe_hardware_defekt
content: |-
  {% if is_state('binary_sensor.pool_pumpe_hardware_defekt', 'on') %}
    PUMPE DEFEKT!
  {% else %}
    Pumpe OK
  {% endif %}
icon: >-
  {{ 'mdi:pump-off' if is_state('binary_sensor.pool_pumpe_hardware_defekt',
  'on')

  else 'mdi:pump' }}
color: |-
  {{ 'crimson' if is_state('binary_sensor.pool_pumpe_hardware_defekt', 'on') 
  else 'limegreen' }}
tap_action:
  action: call-service
  service: button.press
  target:
    entity_id: button.pool_poolpumpe_fehler_reset


```
---

```yaml
type: custom:mushroom-template-badge
entity: sensor.pool_chlor_laufzeit_heute
content: |-
  {% set laufzeit = states('sensor.pool_chlor_laufzeit_heute') | float(0) %}
  {% if laufzeit > 0 %}
    Chlor Heute: {{ states('sensor.pool_chlor_laufzeit_heute') }} min
  {% else %}
    Chlor Heute: 0 min
  {% endif %}
icon: mdi:shimmer
color: |-
  {% if states('sensor.pool_chlor_laufzeit_heute') | float(0) > 0 %}
    limegreen
  {% else %}
    crimson
  {% endif %}
tap_action:
  action: more-info

```
---

```yaml
type: custom:mushroom-template-badge
entity: sensor.pool_wifi_signal
content: "{{ states('sensor.pool_wifi_signal') }} dBm"
icon: |-
  {% set rssi = states('sensor.pool_wifi_signal') | float(0) %}
  {% if rssi >= -50 %}
    mdi:wifi-strength-4
  {% elif rssi >= -60 %}
    mdi:wifi-strength-3
  {% elif rssi >= -70 %}
    mdi:wifi-strength-2
  {% else %}
    mdi:wifi-strength-1-alert
  {% endif %}
color: |-
  {% if states('sensor.pool_wifi_signal') | float(0) <= -70 %}
    crimson
  {% else %}
    limegreen
  {% endif %}
tap_action:
  action: more-info

```
---


Bubble Card

```yaml
type: grid
columns: 2
square: false
cards:
  - type: custom:bubble-card
    card_type: button
    button_type: state
    entity: binary_sensor.pool_frequenzsteuerung_online
    name: Freq.Strg. -  Online
    show_icon: false
    show_state: true
    show_name: true
    sub_button:
      - entity: binary_sensor.pool_frequenzsteuerung_online
        show_background: false
        icon: mdi:check-circle
    styles: >
      ${subButtonIcon[0].setAttribute("icon",
      hass.states['binary_sensor.pool_frequenzsteuerung_online'].state === 'on'
      ? 'mdi:check-circle' : 'mdi:close-circle')}

      .bubble-sub-button-1 {
        color: ${hass.states['binary_sensor.pool_frequenzsteuerung_online'].state === 'on' ? 'limegreen' : 'orange'} !important;
      } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }
  - type: custom:bubble-card
    card_type: button
    button_type: state
    entity: binary_sensor.pool_tuya_w2839_online
    name: Tuya W2839 Online
    show_icon: false
    show_state: true
    show_name: true
    sub_button:
      - entity: binary_sensor.pool_tuya_w2839_online
        show_background: false
        icon: mdi:check-circle
    styles: >
      ${subButtonIcon[0].setAttribute("icon",
      hass.states['binary_sensor.pool_tuya_w2839_online'].state === 'on' ?
      'mdi:check-circle' : 'mdi:close-circle')}

      .bubble-sub-button-1 {
        color: ${hass.states['binary_sensor.pool_tuya_w2839_online'].state === 'on' ? 'limegreen' : 'orange'} !important;
      } } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }
  - type: custom:bubble-card
    card_type: button
    button_type: state
    sub_button:
      main:
        - entity: binary_sensor.pool_warmepumpe_online
          show_background: false
          scrolling_effect: false
          show_name: false
          show_state: false
          show_last_changed: false
          show_last_updated: false
          show_attribute: false
          icon: mdi:check-circle
      bottom: []
    entity: binary_sensor.pool_warmepumpe_online
    name: Wärmepumpe - On
    show_icon: false
    show_state: true
    styles: >
      /* 1. Das Icon dynamisch ändern */

      ${subButtonIcon[0].setAttribute("icon",
      hass.states['binary_sensor.pool_warmepumpe_online'].state === 'on' ?
      'mdi:check-circle' : 'mdi:close-circle')}


      /* 2. Die Farbe des Icons dynamisch ändern */

      .bubble-sub-button-1 {
        color: ${hass.states['binary_sensor.pool_warmepumpe_online'].state === 'on' ? 'limegreen' : 'orange'} !important;
      } } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }
    show_name: true
  - type: custom:bubble-card
    card_type: button
    button_type: state
    entity: binary_sensor.pool_chlorinator_24v_online
    name: Chlorinator - Online
    show_icon: false
    show_state: true
    show_name: true
    sub_button:
      - entity: binary_sensor.pool_chlorinator_24v_online
        show_background: false
        icon: mdi:check-circle
    styles: >
      ${subButtonIcon[0].setAttribute("icon",
      hass.states['binary_sensor.pool_chlorinator_24v_online'].state === 'on' ?
      'mdi:check-circle' : 'mdi:close-circle')}

      .bubble-sub-button-1 {
        color: ${hass.states['binary_sensor.pool_chlorinator_24v_online'].state === 'on' ? 'limegreen' : 'orange'} !important;
      } } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }

```
---

Custom:Vertical Stack (HACS)
Custom: pool monitor (HACS)

```yaml
type: custom:vertical-stack-in-card
cards:
  - type: custom:vertical-stack-in-card
    cards:
      - type: custom:config-template-card
        entities:
          - number.pool_orp_sollwert
        card:
          type: custom:pool-monitor-card
          sensors:
            temperature:
              entity: sensor.pool_wasser_temperatur
              availability_entity: binary_sensor.pool_wassertemperatur_verfugbar
            ph:
              entity: sensor.pool_aktueller_ph_wert
              availability_entity: binary_sensor.pool_tuya_w2839_online
            orp:
              entity: sensor.pool_aktueller_orp_wert
              availability_entity: binary_sensor.pool_tuya_w2839_online
              setpoint: ${states['number.pool_orp_sollwert'].state}
            flow_rate:
              entity: sensor.pool_durchfluss_pumpe_m3_h
              availability_entity: binary_sensor.pool_durchflussmesser_aktiv
              max: 14
              setpoint: 9
              min: 5
          display:
            compact: true
            show_names: true
            show_labels: false
            show_last_updated: false
            show_icons: true
            show_units: true
            gradient: true
            language: de
          colors:
            low: "#fdcb6e"
            warn: "#e17055"
            normal: "#00b894"
            cool: "#00BFFF"
            marker: "#000000"
            hi_low: "#00000099"

```
---

```yaml
type: custom:bubble-card
card_type: button
button_type: state
sub_button:
  main:
    - entity: sensor.pool_elektrolyse_energie_heute
      show_state: true
      name: Heute
      show_name: true
      show_background: true
      show_icon: true
      state_background: false
  bottom:
    - entity: sensor.pool_elektrolyse_spannung
      show_state: true
      show_name: true
      name: Spannung
      show_background: false
    - entity: sensor.pool_elektrolyse_stromstarke
      name: Ampere
      show_name: true
      show_state: true
      show_background: false
entity: sensor.pool_elektrolyse_leistung_wirkrichtung
name: Chlorinator Energy
show_state: true
force_icon: false
grid_options:
  columns: 12
rows: 1.719
styles: |
  /* Das Haupt-Icon einfärben */
  .bubble-icon {
    color: ${parseFloat(hass.states['sensor.pool_elektrolyse_stromstarke'].state) >= 1 ? '#2196F3' : 'white'} !important;
  }
  /* Das Icon im Sub-Button ebenfalls blau färben */
  .bubble-sub-button-icon {
    color: ${parseFloat(hass.states['sensor.pool_elektrolyse_stromstarke'].state) >= 1 ? '#2196F3' : 'inherit'} !important;
  }
  } ha-card {
    /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
    --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
    
    /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
    border: none !important;
    box-shadow: none !important;
  }

```
---

Arbeitsmodus und Timer

```yaml
type: custom:vertical-stack-in-card
cards:
  - type: custom:mushroom-template-card
    primary: Arbeitsmodus
    secondary: >-
      {% if is_state('select.pool_pumpenmodus', '55% Stromsparen') %} Aktuell:
      Stromsparen (55%) {% elif is_state('select.pool_pumpenmodus', '70%
      Badebetrieb') %} Aktuell: Normal (70%) {% elif
      is_state('select.pool_pumpenmodus', '85% Badebetrieb') %} Aktuell: Hoch
      (85%) {% elif is_state('select.pool_pumpenmodus', '100% Badebetrieb') %}
      Aktuell: Maximum (100%) {% else %} {{ states('select.pool_pumpenmodus') }}
      {% endif %}
    icon: mdi:engine-outline
    icon_color: >-
      {{ 'dodgerblue' if
      is_state('binary_sensor.pool_frequenzsteuerung_running', 'on') else 'grey'
      }}
    entity: binary_sensor.pool_frequenzsteuerung_running
    badge_icon: >-
      {% set modus = states('select.pool_pumpenmodus') %} {% if 'Stromsparen' in
      modus %} mdi:leaf {% elif '70%' in modus or '85%' in modus %} mdi:waves {%
      elif '100%' in modus %} mdi:rocket-launch {% elif 'Wartung' in modus %}
      mdi:wrench {% elif 'Winter' in modus %} mdi:snowflake {% else %}
      mdi:help-circle {% endif %}
    badge_color: >-
      {% set modus = states('select.pool_pumpenmodus') %} {% if 'Stromsparen' in
      modus %} limegreen {% elif '70%' in modus %} blue {% elif '85%' in modus
      %} dodgerblue {% elif '100%' in modus %} red {% elif 'Wartung' in modus %}
      orange {% elif 'Winter' in modus %} cyan {% else %} grey {% endif %}
  - type: custom:mushroom-chips-card
    card_mod:
      style: |
        ha-card {
          background: transparent !important;
          border: none !important;
          box-shadow: none !important;
          #padding: 0px 16px 12px 16px !important;
          padding: 0px 10px 30px 10px !important;
          --chip-spacing: 4px;
          --rgb-limegreen: 50, 205, 50;
          --limegreen-color: limegreen;
        }
    chips:
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:leaf
        content: 55%
        icon_color: >-
          {{ 'green' if is_state('select.pool_pumpenmodus', '55% Stromsparen')
          else 'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 55% Stromsparen
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:waves
        content: 70%
        icon_color: >-
          {{ 'blue' if is_state('select.pool_pumpenmodus', '70% Badebetrieb')
          else 'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 70% Badebetrieb
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:waves
        content: 85%
        icon_color: >-
          {{ 'blue' if is_state('select.pool_pumpenmodus', '85% Badebetrieb')
          else 'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 85% Badebetrieb
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:rocket-launch
        content: 100%
        icon_color: >-
          {{ 'red' if is_state('select.pool_pumpenmodus', '100% Badebetrieb')
          else 'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 100% Badebetrieb
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:wrench
        content: Wartung
        icon_color: >-
          {{ 'orange' if is_state('select.pool_pumpenmodus', '0% Wartung') else
          'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 0% Wartung
      - type: template
        entity: select.pool_pumpenmodus
        icon: mdi:snowflake
        content: Winter
        icon_color: >-
          {{ 'cyan' if is_state('select.pool_pumpenmodus', '55% Winterbetrieb')
          else 'disabled' }}
        tap_action:
          action: call-service
          service: select.select_option
          target:
            entity_id: select.pool_pumpenmodus
          data:
            option: 55% Winterbetrieb
  - type: custom:mushroom-template-card
    primary: Pool Timer 1
    secondary: >
      An: {{ states('text.pool_timer_startzeit') }} | Aus: {{
      states('text.pool_timer_stoppzeit') }}
    icon: mdi:pool
    icon_color: >-
      {# Greift direkt auf die 3 Bedingungen im Binary Sensor zu #} {{
      'dodgerblue' if is_state('binary_sensor.pool_timer_status', 'on') else
      'grey' }}
    entity: switch.pool_timer_aktiviert
    badge_icon: >-
      {{ 'mdi:power' if is_state('switch.pool_timer_aktiviert', 'on') else
      'mdi:power-off' }}
    badge_color: >-
      {{ 'limegreen' if is_state('switch.pool_timer_aktiviert', 'on') else
      'crimson' }}
  - type: horizontal-stack
    cards:
      - type: entities
        entities:
          - entity: text.pool_timer_startzeit
            name: Starten um
            icon: mdi:clock-start
          - entity: text.pool_timer_stoppzeit
            name: Beenden um
            icon: mdi:clock-end
        card_mod:
          style:
            hui-text-entity-row:
              $:
                ha-textfield:
                  $: |
                    .mdc-text-field {
                      --mdc-text-field-fill-color: transparent !important;
                      --mdc-text-field-idle-line-color: transparent !important;
                    }
                    .mdc-line-ripple { display: none !important; }
                    input { 
                      text-align: left !important; 
                      padding-left: 0px !important;
                      width: 45px !important;
                    }
            .: |
              ha-card { 
                background: none !important; 
                border: none !important; 
                box-shadow: none !important;
                width: 165px !important;
              }
      - type: horizontal-stack
        cards:
          - type: vertical-stack
            cards:
              - type: custom:button-card
                entity: switch.pool_timer_montag
                name: Montag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                entity: switch.pool_timer_mittwoch
                name: Mittwoch
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                entity: switch.pool_timer_freitag
                name: Freitag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                entity: switch.pool_timer_sonntag
                name: Sonntag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                color_type: blank-card
                styles:
                  card:
                    - height: 12px
          - type: vertical-stack
            cards:
              - type: custom:button-card
                entity: switch.pool_timer_dienstag
                name: Dienstag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                entity: switch.pool_timer_donnerstag
                name: Donnerstag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                entity: switch.pool_timer_samstag
                name: Samstag
                tap_action:
                  action: toggle
                styles:
                  card:
                    - height: 38px
                    - width: 72px
                    - border-radius: 6px
                    - background: rgba(255,255,255,0.05)
                    - border: 1px solid rgba(255,255,255,0.1)
                    - padding: 2px
                    - pointer-events: auto !important
                  grid:
                    - grid-template-areas: "\"i\" \"n\""
                    - grid-template-rows: 1fr auto
                    - align-items: center
                    - justify-items: center
                  name:
                    - font-size: 11px
                    - font-weight: none
                    - color: "#a0a0a0"
                  icon:
                    - width: 12px
                    - color: "#606060"
                state:
                  - value: "on"
                    icon: mdi:check-circle
                    styles:
                      card:
                        - border: 1px solid
                        - box-shadow: 0 0 5px rgba(33, 150, 243, 0.4)
                      icon:
                        - color: "#2196F3"
                      name:
                        - color: var(--primary-text-color);
                  - value: "off"
                    icon: mdi:minus-circle-outline
              - type: custom:button-card
                color_type: blank-card
                styles:
                  card:
                    - height: 38px
                    - width: 72px
              - type: custom:button-card
                color_type: blank-card
                styles:
                  card:
                    - height: 12px

```
---

PopUp Aufruf (Sichtbar)
Einstellung und System Karten

```yaml
type: grid
columns: 2
square: false
cards:
  - type: custom:bubble-card
    card_type: button
    button_type: name
    sub_button:
      main: []
      bottom: []
    name: Einstellungen
    icon: mdi:wrench-cog
    grid_options:
      columns: 6
      rows: 2
    button_action:
      tap_action:
        action: navigate
        navigation_path: "#pool-config"
    styles: |
      .card-content {
        width: 100%;
        margin: 0 !important;
      }
      .bubble-button {
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important; /* Zentriert beides als Block */
        padding-top: 20px !important;
        /* Diese Transition steuert das ZURÜCKGEHEN (De-Transition) */
        transition: background-color 0.1s ease-in-out !important;
      }
      .bubble-icon-container {
        background: none !important;
        margin-right: 5px !important; /* Wichtig bei Spalten-Layout */
        margin-bottom: -30px !important; /* Standard-Lücke entfernen */
        min-width: 0px !important; 
        min-height: 0px !important;
      }
      .bubble-icon {
        --mdc-icon-size: 32px !important;
      }
      .bubble-name {
        font-size: 15px !important;
        font-weight: 500 !important;
        text-align: center !important;
        margin-top: -10px !important; /* Zieht den Text näher ans Icon */
      }
      /* Korrektur des Hover-Hintergrunds */
      .bubble-button-background {
        opacity: 0 !important; /* Den Standard-Background-Effekt abschalten... */
      }
      /* ...und stattdessen den echten Button-Hintergrund beim Hover färben */
      .bubble-button:hover {
        background-color: rgba(255, 255, 255, 0.05) !important;
        transition: 0s !important;
      }
      } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }
  - type: custom:bubble-card
    card_type: button
    button_type: name
    sub_button:
      main: []
      bottom: []
    name: System
    icon: mdi:monitor-dashboard
    grid_options:
      columns: 6
      rows: 2
    button_action:
      tap_action:
        action: navigate
        navigation_path: "#system-info"
    styles: |
      .card-content {
        width: 100%;
        margin: 0 !important;
      }
      .bubble-button {
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important; /* Zentriert beides als Block */
        padding-top: 20px !important;
        /* Diese Transition steuert das ZURÜCKGEHEN (De-Transition) */
        transition: background-color 0.1s ease-in-out !important;
      }
      .bubble-icon-container {
        background: none !important;
        margin-right: 15px !important; /* Wichtig bei Spalten-Layout */
        margin-bottom: -30px !important; /* Standard-Lücke entfernen */
        min-width: 0px !important; 
        min-height: 0px !important;
      }
      .bubble-icon {
        --mdc-icon-size: 32px !important;
      }
      .bubble-name {
        font-size: 15px !important;
        font-weight: 500 !important;
        text-align: center !important;
        margin-top: -10px !important; /* Zieht den Text näher ans Icon */
      }
      /* Korrektur des Hover-Hintergrunds */
      .bubble-button-background {
        opacity: 0 !important; /* Den Standard-Background-Effekt abschalten... */
      }
      /* ...und stattdessen den echten Button-Hintergrund beim Hover färben */
      .bubble-button:hover {
        background-color: rgba(255, 255, 255, 0.05) !important;
        transition: 0s !important;
      }
      } ha-card {
        /* Erzwingt die Standard-Hintergrundfarbe deines Themes */
        --bubble-main-background-color: var(--ha-card-background, var(--card-background-color, var(--ha-card-fill-color, #2a2a2a))) !important;
        
        /* Entfernt eventuelle Schatten oder Rahmen, falls nötig */
        border: none !important;
        box-shadow: none !important;
      }

```
---

PopUp: Einstellung (Unsichtbar)


```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    name: Pool Konfiguration
    icon: mdi:pool
    hash: "#pool-config"
    button_type: name
    slide_to_close_distance: "590"
  - type: custom:bubble-card
    card_type: separator
    name: Pumpe & Durchfluss
  - square: false
    type: grid
    cards:
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_poolpumpe_vorlaufzeit_min
        name: Vorlauf
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_durchfluss_poolpumpe_100
        name: Durchfluss 100%
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
    columns: 2
  - type: custom:bubble-card
    card_type: select
    button_type: switch
    entity: select.pool_durchflussmesser_installiert
    name: Flow Sensor?
    show_state: true
    show_attribute: false
    attribute: friendly_name
  - type: custom:bubble-card
    card_type: separator
    name: ORP Konfig
    icon: mdi:shimmer
  - type: grid
    columns: 2
    square: false
    cards:
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_orp_sollwert
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_orp_min_wert
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_orp_max_wert
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
  - type: custom:bubble-card
    card_type: separator
    name: Chlorinator
    icon: mdi:water-percent
  - type: grid
    columns: 2
    square: false
    cards:
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_chlorinator_max_laufzeit_zyklus_min
        name: Max Zyklus
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_chlorinator_max_laufzeit_tag
        name: Max Tag
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_lowsalt_limit
        name: Low Salt Limit
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
  - type: custom:bubble-card
    card_type: separator
    name: PH Konfig
    icon: mdi:ph
  - type: grid
    columns: 2
    square: false
    cards:
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_forderleistung_l_h
        name: Förderleistung
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_kanister_grosse
        name: Kanister
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_max_pro_zyklus
        name: Max/Zyklus
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_max_pro_tag
        name: Max/Tag
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_min_wert_wasser
        name: Min Wasser
        show_state: true
      - type: custom:bubble-card
        card_type: button
        button_type: slider
        entity: number.pool_ph_max_wert_wasser
        name: Max Wasser
        show_state: true
        sub_button:
          main: []
          bottom: []
        button_action:
          tap_action:
            action: none
          double_tap_action:
            action: more-info
        tap_action:
          action: none
        relative_slide: true

```
---

PopUp System Monitor (unsichtbar)

```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    name: System Monitor
    icon: mdi:monitor-dashboard
    hash: "#system-info"
    button_type: name
    sub_button:
      main: []
      bottom: []
  - type: grid
    columns: 2
    square: false
    cards:
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_temperatur_pool_controller
        name: Controller Temp
        show_state: true
        icon: ""
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_letzter_restart_grund
        name: Letzter Neustart
        show_state: true
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_betriebszeit_seit_boot
        name: Betriebszeit
        show_state: true
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_wifi_ssid
        name: WiFi Name
        show_state: true
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_wifi_signal
        name: WiFi Signal
        show_state: true
      - type: custom:bubble-card
        card_type: button
        button_type: state
        entity: sensor.pool_wifi_ip
        name: IP Adresse
        show_state: true
  - type: custom:bubble-card
    card_type: button
    button_type: switch
    entity: switch.pool_neustart_normal
    name: Controller Neustart
    show_state: true
    button_action:
      tap_action:
        action: more-info
      hold_action:
        action: toggle

```
---

PopUp PoolPumpe Laufzeit Tag (Unsichtbar)

```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    name: Pumpenlaufzeit Tag
    icon: mdi:chart-bar
    hash: "#pool-day-runtime"
  - type: grid
    columns: 1
    square: false
    cards:
      - type: custom:apexcharts-card
        update_delay: 500ms
        graph_span: 7d
        header:
          show: true
          title: Pumpenlaufzeit (7 Tage)
          show_states: true
        span:
          end: day
        apex_config:
          chart:
            height: 300px
            animations:
              enabled: false
          redrawOnParentResize: true
        series:
          - entity: sensor.pool_pumpen_laufzeit_heute
            type: column
            name: Stunden
            color: "#00b894"
            group_by:
              func: max
              duration: 1d
            transform: return x;
            show:
              datalabels: true

```
---

```yaml

```




